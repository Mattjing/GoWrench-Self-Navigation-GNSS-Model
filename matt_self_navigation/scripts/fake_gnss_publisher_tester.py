#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus
import time

def fake_gnss_publisher():
    rospy.init_node('fake_gnss_publisher', anonymous=True)
    # Publish to the specific ETHZ package topic for GNSS data
    pub = rospy.Publisher('/piksi/navsatfix_best_fix', NavSatFix, queue_size=10)
    # Famous landmark coordinates (latitude, longitude, altitude)
    landmarks = [
        {"name": "Eiffel Tower", "latitude": 48.8584, "longitude": 2.2945, "altitude": 10.0},
        {"name": "Statue of Liberty", "latitude": 40.6892, "longitude": -74.0445, "altitude": 10.0},
        {"name": "Great Wall of China", "latitude": 40.4319, "longitude": 116.5704, "altitude": 10.0},
        {"name": "Pyramids of Giza", "latitude": 29.9792, "longitude": 31.1342, "altitude": 10.0},
        {"name": "Sydney Opera House", "latitude": -33.8568, "longitude": 151.2153, "altitude": 10.0}
    ]

    rate = rospy.Rate(1)  # 1 Hz, publish once per second

    for landmark in landmarks:
        rospy.loginfo(f"Publishing location: {landmark['name']}")
        start_time = time.time()
        while time.time() - start_time < 5:  # Publish each location for 5 seconds
            msg = NavSatFix()

            # Set the landmark's coordinates
            msg.latitude = landmark["latitude"]
            msg.longitude = landmark["longitude"]
            msg.altitude = landmark["altitude"]

            # Simulate a valid GNSS fix
            msg.status.status = NavSatStatus.STATUS_FIX
            msg.status.service = NavSatStatus.SERVICE_GPS

            # Set the covariance (to simulate the GPS accuracy)
            msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
            msg.position_covariance = [0.0001, 0, 0,
                                       0, 0.0001, 0,
                                       0, 0, 0.0001]

            # Publish the GNSS data for the landmark
            pub.publish(msg)
            rospy.loginfo(f"Publishing GNSS data: {landmark['name']} - Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}")
            rate.sleep()

    rospy.loginfo("Finished publishing coordinates for all landmarks.")

if __name__ == '__main__':
    try:
        fake_gnss_publisher()
    except rospy.ROSInterruptException:
        pass
