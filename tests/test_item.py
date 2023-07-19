import pytest
from src.item import Item
#from maim import item1, item2
item1 = Item('Смартфон', 10000, 20)
item2 = Item('Телефон', 5000, 10)
def test_calculate_total_price(self):
    assert item1.calculate_total_price() == 200000.0

def test_apply_discount():
    item3 = Item('Смартфон', 1000, 10)
    print(item3)
    Item.pay_rate = 0.7
    item3.apply_discount()
    assert item3.price == 700


def test_name():
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert item1.string_to_number('20') == 20

def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Телефон', 5000, 10)"

def test_str():
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Телефон'

def test_instantiate_from_csv():
    assert Item.instantiate_from_csv('item.csv') == "FileNotFoundError: Отсутствует файл item.csv"
