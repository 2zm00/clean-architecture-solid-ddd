"""
DDD - Service 예제
"""

class OrderService:
    def __init__(self, order_repository):
        self.repo = order_repository

    def change_order_customer(self, order_id, new_name):
        order = self.repo.find_by_id(order_id)
        if order:
            order.change_customer(new_name)
