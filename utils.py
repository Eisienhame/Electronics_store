import csv

class Item:

    num_of_items = []
    discount_price = 1

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity



        Item.num_of_items.append(self.__name)

    @property
    def name(self, name=None):
        if name == None:
            return self.__name
        else:
            self.__name = name
            return self.__name



    @name.setter
    def name(self, name : str):
        if len(name) > 10:
             raise Exception('Длина наименования товара превышает 10 символов.')
        else:
             self.__name = name



    def calculate_total_price(self):
        return (self.price * self.quantity)

    def apply_discount(self):
        self.price = (self.price * Item.discount_price)