from utils import Item

Item.load_from_csv('items.csv')  # создание объектов из данных файла
print(len(Item.num_of_items))  # в файле 5 записей с данными по товарам
print(Item.num_of_items[4])
item1 = Item.num_of_items[0]
print(item1)

test_item = Item("Смартфон", 10000, 10)
test_item.name = 'ДлинаСмартфон'