from typing import Dict, Iterator, List


class Product:
    """Класс для представления товара с приватной ценой и методами доступа"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.quantity: int = quantity
        self.price = price

    @classmethod
    def new_product(cls, data: Dict) -> "Product":
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
        """Возвращает строку вида: Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Реализует сложение двух объектов Product. Возвращает общую стоимость склада этих двух товаров"""
        if not isinstance(other, Product):
            return NotImplemented

        total_a = self.price * self.quantity
        total_b = other.price * other.quantity
        return total_a + total_b


class Category:
    """Класс для представления категории товаров. Список товаров является приватным атрибутом"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] | None = None) -> None:
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

    @property
    def _product_list(self) -> List[Product]:
        """Предоставляет внутренний список товаров для класса-итератора."""
        return self.__products

    def __str__(self) -> str:
        """
        Возвращает строку вида: Название категории, количество продуктов: X шт.
        Подсчитывает общее количество всех товаров на складе в этой категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator(Iterator):
    """Класс для итерации по товарам одной категории"""

    def __init__(self, category: Category):
        self._items = category._product_list
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        """Метод возвращает сам объект-итератор."""
        return self

    def __next__(self) -> Product:
        """Метод возвращает следующий товар или поднимает StopIteration."""
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration
