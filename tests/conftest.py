import pytest
from utils import Item
@pytest.fixture
def item_test():
    x = Item(name='ТОВАР', price=10000, quantity=20)
    return x

@pytest.fixture
def item_test2():
    x = Item(name='ТОВАРТОВАРТОВАР', price=10000, quantity=20)
    return x