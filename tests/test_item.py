import pytest
from src.item import Item
#from maim import item1, item2
item1 = Item("Смартфон", 10000, 20)
def test_calculate_total_price(self):
    assert item1.calculate_total_price() == 200000.0

def test_apply_discount():
    item3 = Item("Смартфон", 1000, 10)
    print(item3)
    Item.pay_rate = 0.7
    item3.apply_discount()
    assert item3.price == 700

