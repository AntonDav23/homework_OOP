from src.base_product import BaseProduct
from src.product_mixin import CreationLoggerMixin
from typing import Dict


class Product(BaseProduct):
    """ Класс реализации базового продукта """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
       """Геттер для приватного атрибута цены"""
       return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self) -> str:
        """Возвращает строку вида: Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Реализует сложение двух объектов Product"""
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать товары разных типов: {type(self).__name__} и {type(other).__name__}")

        total_a = self.price * self.quantity
        total_b = other.price * other.quantity
        return total_a + total_b


    @classmethod
    def new_product(cls, data: Dict[str, object]) -> 'Product':
        return cls(name=data['name'],description=data['description'], price=data['price'], quantity=data['quantity'])


class LoggedProduct(CreationLoggerMixin, BaseProduct):
    """ Промежуточный класс, объединяющий логику логирования и структуры продукта """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, data: Dict[str, object]) -> 'LoggedProduct':
        return cls(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'])

Product = LoggedProduct