import csv

class Item:

    num_of_items = []  #общий спсисок предметов
    discount_price = 1 #ставка

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.num_of_items.append(self.__name)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.quantity})'

    def __str__(self):
        return self.__name

    def __add__(self, other):
#        if ((isinstance(self, Item) or issubclass(self.__class__, Item)) is True) and ((issubclass(other.__class__, Item) or isinstance(other, Item)) is True):
        if self.__class__ == other.__class__:
            return int(self.quantity) + int(other.quantity)
        else:
            return 'Сложение запрещено'


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

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        self.sim_count = number_of_sim
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.quantity}), {self.number_of_sim}'

    @property
    def number_of_sim(self, number_of_sim=None):
        if number_of_sim == None:
            return self.number_of_sim
        else:
            self.number_of_sim = number_of_sim
            return self.number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
             self.number_of_sim = number_of_sim