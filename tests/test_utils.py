import pytest

from utils import Item, Phone, Keyboard



def test_calculate_total_price():
    test_item = Item("Смартфон", 10000, 10)
    assert test_item.calculate_total_price() == 100000
    test_item.apply_discount()
    assert test_item.price == 10000

def test_is_int():
    assert Item.is_int(5) is True
    assert Item.is_int(5.8) is False
    assert Item.is_int('') is False

def test_load_from_csv():
    Item.load_from_csv('items.csv')
    assert len(Item.num_of_items) == 6
    assert Item.num_of_items[0] == 'Смартфон'

def test_get_file_not_found_error():
    "Test исключения FileNotFoundError в связи с отсутствием файла"""
    Item.load_from_csv('irtems.csv')
    assert Item.load_from_csv('irtems.csv') == print(f"По указанному пути файл irtems.csv отсутствует")
def test_name_setter():
    test_item = Item("Смартфон", 10000, 10)
    test_item.name = 'Длина'
    assert test_item.name == 'Длина'

def test_repr(item_test):
    assert repr(item_test) == 'Item("ТОВАР", 10000, 20)'

def test_str(item_test):
    assert str(item_test) == 'ТОВАР'

def test_raises(item_test2):
    with pytest.raises(Exception):
         item_test2.name = 'Длина наименования товара превышает 10 символов.'

def test_phone_number_of_sim():
    test_item = Phone("Смартфон", 10000, 10, 2)
    test_item2 = Phone("Смартфон2", 10000, 3, 2)
    test_item3 = Item("Смартфон", 10000, 10)
    assert test_item.number_of_sim == 2
    assert test_item + test_item2 == 13
    assert test_item3 + test_item2 == 'Сложение запрещено'

def test_value(item_test3):
    with pytest.raises(Exception):
         item_test3.name = 'Количество физических SIM-карт должно быть целым числом больше нуля.'

def test_langage(item_test4):
    item_test4.change_lang()
    assert item_test4.language == 'RU'

