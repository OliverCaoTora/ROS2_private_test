from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package= 'int32_topic_pkg',
            executable= 'int32_publischer'
        ),
        Node(
            package= 'int32_topic_pkg',
            executable= 'int32_subscriber'
        )
    ])