#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus

def fake_gnss_publisher():
    rospy.init_node('fake_gnss_publisher', anonymous=True)
     # Publish to the specific ETHZ package topic for GNSS data
    pub = rospy.Publisher('/piksi/navsatfix_best_fix', NavSatFix, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        msg = NavSatFix()

        # Set a fake, static position (e.g., latitude and longitude for a specific location)
        msg.latitude = 37.7749  # Replace with desired test latitude
        msg.longitude = -122.4194  # Replace with desired test longitude
        msg.altitude = 10.0  # Replace with desired altitude

        # Simulate a valid GNSS fix
        msg.status.status = NavSatStatus.STATUS_FIX
        msg.status.service = NavSatStatus.SERVICE_GPS

        # Optionally set the covariance (to simulate the GPS accuracy)
        msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
        msg.position_covariance = [0.0001, 0, 0,
                                   0, 0.0001, 0,
                                   0, 0, 0.0001]

        # Publish the fake GNSS data
        pub.publish(msg)
        rospy.loginfo(f"Publishing fake GNSS data: Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}")
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_gnss_publisher()
    except rospy.ROSInterruptException:
        pass

