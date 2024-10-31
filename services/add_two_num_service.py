from kz_interfaces.srv import AddTwoNum

import rclpy
from rclpy.node import Node

class MiniSumService(Node):

    def __init__(self):
        super().__init__('mini_sum_service')
        self.srv = self.create_service(AddTwoNum, 'add_two_num', self.add_two_num_callback)

    def add_two_num_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MiniSumService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()