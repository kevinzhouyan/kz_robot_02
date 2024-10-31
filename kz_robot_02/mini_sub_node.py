import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String

class MiniSubNode(Node):

    def __init__(self):
        super().__init__('mini_subscriber')
        self.subscription = self.create_subscription(
            String,
            'kztopic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    try:
        rclpy.init(args=args)
        mini_subscriber = MiniSubNode()

        rclpy.spin(mini_subscriber)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()