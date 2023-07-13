from src.item import Item

class Mixin:
    kb_language = "EN"
    def __init__(self):
        self.language = self.kb_language

    def change_lang(self):
        self.language = "RU"
        return self.language

class KeyBoard(Item, Mixin):
    """
    дочерний класс.
    """
    def __init__(self, name: str, price: float, quantity: int, language: str):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.language = language
        self.__name = name

