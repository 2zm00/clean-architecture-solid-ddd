"""
OCP - 개방-폐쇄 원칙
확장에는 열려 있고 변경에는 닫혀 있어야 한다.
"""

class Discount:
    def get_discount(self, price):
        return price

class StudentDiscount(Discount):
    def get_discount(self, price):
        return price * 0.8

class SeniorDiscount(Discount):
    def get_discount(self, price):
        return price * 0.9

def apply_discount(discount_strategy: Discount, price):
    return discount_strategy.get_discount(price)

if __name__ == "__main__":
    print(apply_discount(StudentDiscount(), 100))
    print(apply_discount(SeniorDiscount(), 100))
