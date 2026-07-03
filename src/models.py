from typing import Dict, List


class Product:
    """Класс для представления товара с приватной ценой и методами доступа"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.quantity: int = quantity
        self.price = price

    @classmethod
    def new_product(cls, data: Dict) -> 'Product':
        """Класс-метод для создания объекта Product из словаря"""
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

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
        """Внутренний метод для красивого вывода информации о товаре"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс для представления категории товаров.Список товаров является приватным атрибутом"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]  | None = None) -> None:
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = []

        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в приватный список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, который возвращает информацию о товарах в виде отформатированной строки"""
        if not self.__products:
            return "Товаров в категории нет."

        return "\n".join(str(product) for product in self.__products)
