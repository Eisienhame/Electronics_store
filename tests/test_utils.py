import pytest

from utils import Item



def test_calculate_total_price():
    test_item = Item("Смартфон", 10000, 10)
    assert test_item.calculate_total_price() == 100000
    test_item.apply_discount()
    assert test_item.price == 10000

