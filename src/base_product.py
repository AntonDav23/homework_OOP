from typing import Dict


class Product:
    """ Базовый (родительский) класс для предоставления товара """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.quantity: int = quantity
        self.price = price

    @classmethod
    def new_product(cls, data: Dict) -> "Product":
        """ Класс-метод для создания объекта Product из словаря """
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

    @property
    def price(self) -> float:
        """ Геттер для приватного атрибута цены """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """ Сеттер для цены с валидацией """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self) -> str:
        """Возвращает строку вида: Название продукта, X руб. Остаток: X шт. """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """ Реализует сложение двух объектов Product """
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать товары разных типов: {type(self).__name__} и {type(other).__name__}")

        total_a = self.price * self.quantity
        total_b = other.price * other.quantity
        return total_a + total_b
