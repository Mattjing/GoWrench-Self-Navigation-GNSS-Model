#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus
import random

def fake_gnss_publisher():
    rospy.init_node('fake_gnss_publisher', anonymous=True)
     # Publish to the specific ETHZ package topic for GNSS data
    pub = rospy.Publisher('/piksi/navsatfix_best_fix', NavSatFix, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    # Initial position
    latitude = 37.7749  # Base latitude
    longitude = -122.4194  # Base longitude
    altitude = 10.0  # Base altitude

    while not rospy.is_shutdown():
        msg = NavSatFix()

        # Modify latitude, longitude, and altitude slightly each time
        latitude += random.uniform(-0.001, 0.001)  # Small change in latitude
        longitude += random.uniform(-0.001, 0.001)  # Small change in longitude
        altitude += random.uniform(-0.1, 0.1)  # Small change in altitude

        msg.latitude = latitude
        msg.longitude = longitude
        msg.altitude = altitude

        # Simulate a valid GNSS fix
        msg.status.status = NavSatStatus.STATUS_FIX
        msg.status.service = NavSatStatus.SERVICE_GPS

        # Optionally set the covariance (to simulate GPS accuracy)
        msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
        msg.position_covariance = [0.0001, 0, 0,
                                   0, 0.0001, 0,
                                   0, 0, 0.0001]

        # Publish the fake GNSS data
        pub.publish(msg)
        rospy.loginfo(f"Publishing dynamic fake GNSS data: Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}")
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_gnss_publisher()
    except rospy.ROSInterruptException:
        pass
