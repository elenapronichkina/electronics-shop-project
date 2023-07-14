from src.item import Item

class Mixin:
    kb_language = "EN"
    def __init__(self):
        self.language = self.kb_language
    @property
    def get_language(self):
        return self.language
    def change_lang(self):
        kb_language = "EN"
        if self.language == kb_language:
            self.language = "RU"
        else:
            self.language = "EN"
        return self.language

class KeyBoard(Item, Mixin):
    """
    дочерний класс.
    """
    def __init__(self, name: str, price: float, quantity: int, language):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.language = language
        self.__name = name

