from utils import Item, Phone, Keyboard, Mixin_lang

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 25", 120_000, 2, 2)
phone3 = Item("iPhone 25", 120_000, 2)

kb = Keyboard('Dark Project KD87A', 9600, 5)
print(kb)
print(kb.language)
kb.change_lang()
print(kb.language)

kb.language = 'CH'