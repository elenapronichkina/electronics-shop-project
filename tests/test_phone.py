import pytest
from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 11", 50_000, 3, 2)
item1 = Item("Смартфон", 10000, 20)

def test_repr_phone():
    assert repr(phone1) == "Phone('iPhone 14', 120_000, 5, 2)"

def test_str():
    assert str(phone2) == 'iPhone 11'

def test_add():
    assert item1 + phone1 == 25
    assert phone1 + phone2 == 4