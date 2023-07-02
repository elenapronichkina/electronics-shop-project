from src.item import Item
class Phone(Item):
    """
    дочерний класс для представления товара в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.number_of_sim = number_of_sim
        self.__name = name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
         return self.number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """проверяет, что количество физических SIM-карт - целще число больше нуля"""

        #if int(number_of_sim)/float(number_of_sim) == 1.0 and number_of_sim > 0:
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
