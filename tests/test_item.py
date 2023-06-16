import pytest
from src.item import Item
from maim import item1, item2
#item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price(self):
    assert item1.calculate_total_price() == 200000.0


def test_apply_discount(self):
    assert item1.apply_discount() == 8000.0