import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    share_dir = get_package_share_directory('lio_sam')

    return LaunchDescription([
        Node(
            package='imu_filter_madgwick',
            executable='imu_filter_madgwick_node',
            name='imu_filter',
            output='screen',
            parameters=[os.path.join(share_dir, 'config', 'imu_filter.yaml')],
            remappings=[('/imu/data_raw', '/livox/imu')]
        )
    ])
