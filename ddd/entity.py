"""
DDD - Entity 예제
"""

from dataclasses import dataclass

@dataclass
class Order:
    order_id: int
    customer_name: str

    def change_customer(self, new_name):
        self.customer_name = new_name
