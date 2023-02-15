
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount_price = 1

    def calculate_total_price():
        return (self.price * self.quantity)

    def apply_discount():
        self.price = self.price * self.discount_price