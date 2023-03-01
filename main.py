from utils import Item, Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 25", 120_000, 2, 2)
phone3 = Item("iPhone 25", 120_000, 2)
phone1.number_of_sim = 1
print(phone1.number_of_sim)