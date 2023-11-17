import rclpy
from geometry_msgs.msg import Twist
import sys
import os

os.system("ros2 run gazebo_ros spawn_entity.py -database prius_hybrid  -entity PR001 -x 93 -y -11.7  -Y -1.57")
os.system("ros2 run gazebo_ros spawn_entity.py -database prius_hybrid  -entity PR002 -x 93 -y -15.9  -Y -1.57")

def control_vehicle(vehicle_name):
    node = rclpy.create_node('vehicle_controller')
    twist_pub = node.create_publisher(Twist, f'{vehicle_name}/cmd_vel', 10)

    # 사용자 입력을 대신하여 원하는 값을 직접 입력
    linear_speed = 1.0
    angular_speed = 0.5

    while rclpy.ok():
        twist_msg = Twist()
        twist_msg.linear.x = linear_speed
        twist_msg.angular.z = angular_speed

        twist_pub.publish(twist_msg)
        rclpy.spin_once(node)
        print(f"Published Twist message: {twist_msg}")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 control_spawned_vehicle.py <vehicle_name>")
        sys.exit(1)

    vehicle_name = sys.argv[1]

    rclpy.init()
    try:
        control_vehicle(vehicle_name)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
