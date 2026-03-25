import requests
import polyline
import rospy
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus


def get_route_coordinates(api_key, origin, destination):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key,
        "mode": mode
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "OK":
        coordinates = []
        for leg in data["routes"][0]["legs"]:
            for step in leg["steps"]:
                points = polyline.decode(step["polyline"]["points"])
                coordinates.extend(points)
        return coordinates
    else:
        print("Error fetching route:", data["status"])
        return []


def fake_gnss_publisher(api_key, origin, destination):
    rospy.init_node('fake_gnss_publisher', anonymous=True)
    pub = rospy.Publisher('/piksi/navsatfix_best_fix', NavSatFix, queue_size=10)
    rate = rospy.Rate(1)

    # Get coordinates from Google Maps API
    coordinates = get_route_coordinates(api_key, origin, destination)

    for lat, lon in coordinates:
        if rospy.is_shutdown():
            break

        msg = NavSatFix()
        msg.latitude = lat
        msg.longitude = lon
        msg.altitude = 10.0
        msg.status.status = NavSatStatus.STATUS_FIX
        msg.status.service = NavSatStatus.SERVICE_GPS

        pub.publish(msg)
        rospy.loginfo(f"Publishing GNSS data: Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}")
        rate.sleep()


if __name__ == '__main__':
    # Define your API key, origin, and destination
    api_key = "AIzaSyBJXqeYsRZaNtO2B5YilmMUBG30cdT0JfQ"
    origin = "Times Square, New York, NY"
    destination = "Central Park, New York, NY"
    mode = 'walking'

    try:
        fake_gnss_publisher(api_key, origin, destination, mode)
    except rospy.ROSInterruptException:
        pass
