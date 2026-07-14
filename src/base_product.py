from abc import ABC, abstractmethod
from typing import Dict


class BaseProduct(ABC):
    """ Абстрактный базовый класс для всех продуктов """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self._price = price  # Защищенный атрибут для доступа через property

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены. Должен быть реализован в дочерних классах."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Строковое представление товара. Каждый продукт должен уметь выводить себя в консоль по-своему """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: Dict[str, object]) -> 'BaseProduct':
        """ метод для создания объекта из словаря """
        pass