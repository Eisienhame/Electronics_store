from utils import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price(), '- общая стоимость смартфонов')
print(item2.calculate_total_price(), '- общая стоимость ноутбуков')

Item.discount_price = 0.8
item1.apply_discount()
print(item1.price, '- к цене смартфона применена скидка')
print(item2.price, '- к цене ноутбука скидка не была применена')

print(Item.num_of_items)