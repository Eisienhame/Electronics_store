from utils import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price(), '- общая стоимость смартфонов')
print(item2.calculate_total_price(), '- общая стоимость ноутбуков')

item1.name = 'СуперСмартфон'
print(item1.name)
print(Item.num_of_items)