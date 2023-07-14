from src.item import Item

class Mixin:
    kb_language = "EN"
    def __init__(self):
        self.__language = self.kb_language
    @property
    def language(self):
        return self.__language
    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

class KeyBoard(Item, Mixin):
    """
    дочерний класс.
    """
    def __init__(self, name: str, price: float, quantity: int, language):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        # self.language = language
        # self.__name = name

