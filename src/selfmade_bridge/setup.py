from setuptools import setup

package_name = 'selfmade_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Martin Howecker',
    maintainer_email='mhowecker@student.tgm.ac.at',
    description='A custom try to bridge ROS2 to ROS1',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'bridge = selfmade_bridge.bridge_listener:main',
        ],
    },
)
