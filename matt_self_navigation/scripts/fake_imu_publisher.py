#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
import tf.transformations

def fake_imu_publisher():
    rospy.init_node('fake_imu_publisher', anonymous=True)
    pub = rospy.Publisher('/imu/data', Imu, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        imu_msg = Imu()
        # Simulate an orientation in quaternion (no rotation)
        quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
        imu_msg.orientation = Quaternion(*quaternion)
        # Simulate no angular velocity and no linear acceleration
        imu_msg.angular_velocity.x = 0.0
        imu_msg.angular_velocity.y = 0.0
        imu_msg.angular_velocity.z = 0.0
        imu_msg.linear_acceleration.x = 0.0
        imu_msg.linear_acceleration.y = 0.0
        imu_msg.linear_acceleration.z = 0.0

        # Publish the fake IMU data
        pub.publish(imu_msg)
        rospy.loginfo("Publishing fake IMU data")
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_imu_publisher()
    except rospy.ROSInterruptException:
        pass
