
class Item:

    num_of_items = 0
    discount_price = 1

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


        Item.num_of_items += 1

    def calculate_total_price():
        return (self.price * self.quantity)

    def apply_discount():
        self.price = self.price * Item.discount_price