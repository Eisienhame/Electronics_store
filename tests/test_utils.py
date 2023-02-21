import pytest

from utils import Item



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
def test_name_setter():
    test_item = Item("Смартфон", 10000, 10)
    test_item.name = 'Длина'
    assert test_item.name == 'Длина'

def test_str():
    test_item = Item("Смартфон", 10000, 10)
    assert test_item == 'Item("Смартфон", 10000, 10)'

# @pytest.fixture
# def item_test():
#     return Item(name='ТОВАРТОВАРТОВАР', price=10000, quantity=20)

 # def test_raises(item_test):
 #     with pytest.raises(Exception):
 #         item_test.name = 'Длина наименования товара превышает 10 символов.'