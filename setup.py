from setuptools import find_packages, setup

package_name = 'kz_robot_02'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kevin',
    maintainer_email='kevinzhouyan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kz_mini_pub_node = kz_robot_02.mini_pub_node:main',
            'kz_mini_sub_node = kz_robot_02.mini_sub_node:main',
            'kz_sum_service = services.add_two_num_service:main',
            'kz_sum_client = services.add_two_num_client:main',
        ],
    },
)
