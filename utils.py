import csv

class Item:

    num_of_items = []
    discount_price = 1

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity



        Item.num_of_items.append(self.__name)

    # @name.setter
    # def name(self, name : str):
    #     if len(self.__name) > 10:
    #         raise Exception('Длина наименования товара превышает 10 символов.')
    #     else:
    #         self.__name = name




    def calculate_total_price(self):
        return (self.price * self.quantity)

    def apply_discount(self):
        self.price = (self.price * Item.discount_price)