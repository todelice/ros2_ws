from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py',
            arguments=['-entity', 'your_model_name', '-file', '/home/robotik/ros2_ws/src/robot_spawner/urdf/Montaj1/urdf/Montaj1.urdf'],
            output='screen'
        ),
    ])
