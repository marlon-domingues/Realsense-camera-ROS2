from setuptools import find_packages, setup

package_name = 'RGBD_data'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='md00126',
    maintainer_email='md00126@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "realsense_pub = RGBD_data.realsense_pub:main",
            "realsense_sub = RGBD_data.realsense_sub:main"
        ],
    },
)
