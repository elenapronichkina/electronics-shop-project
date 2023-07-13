from src.keyboard import KeyBoard

kb1 = KeyBoard('KD87A', 1000, 5)
def test_name(self):
    assert str(kb1) == "KD87A"

def test_language():
    assert str(kb1.language) == "EN"

def test_change_lang():
    assert str(kb1.language) == "RU"

