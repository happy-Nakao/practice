#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import Twist

def operator():
    rclpy.init_node('operator', anonymous=True)
    pub = rclpy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 2.0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 1.8
    
    rate = rclpy.Rate(1) # 1hz
    while not rclpy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        operator()
    except rclpy.ROSInterruptException:
        pass
