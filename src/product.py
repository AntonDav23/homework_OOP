from typing import Dict

from .base_product import BaseProduct
from .product_mixin import CreationLoggerMixin


class Product(CreationLoggerMixin, BaseProduct):
    """Класс реализации базового продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены"""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self) -> str:
        """Возвращает строку вида: Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return self.__str__()


    @classmethod
    def new_product(cls, data: Dict) -> "Product":
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

    def __add__(self, other: "BaseProduct") -> float:
        """Реализует сложение двух объектов Product"""

        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать товары разных типов: {type(self).__name__} и {type(other).__name__}")

        total_a = self.price * self.quantity
        total_b = other.price * other.quantity
        return total_a + total_b
