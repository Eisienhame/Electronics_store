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
    #
    @name.setter
    def name(self, name : str):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')

            #print('Exception: Длина наименования товара превышает 10 символов.')
        else:
             self.__name = name

    @classmethod
    def load_from_csv(cls, data):
        with open(data) as file:
            csv_table = csv.DictReader(file)
            for row in csv_table:
                cls(name = row['name'],
                    price = float(row['price']),
                     quantity = int(row['quantity']))
    @staticmethod
    def is_int(number):
        if isinstance(number, int) or isinstance(number, float) and number % 1 == 0:
            return True
        else:
            return False


    def calculate_total_price(self):
        return (self.price * self.quantity)

    def apply_discount(self):
        self.price = (self.price * Item.discount_price)