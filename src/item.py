import csv
import os.path
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        """инициализирует экземпляры класса Item данными из файла src/items.csv"""
        with open(os.path.join(os.path.dirname(__file__)), 'items.csv', newline='', encoding="windows-1251") as csvfile:
            cls.all = []
            reader = csv.DictReader(csvfile)
            for row in reader:
              name = row['name']
              price = row['price']
              quantity = row['quantity']
              cls(name, price, quantity)

            #print(cls)


    @staticmethod
    def string_to_number(quantity):
        """возвращает число из числа-строки"""
        number = int(quantity)
        return number