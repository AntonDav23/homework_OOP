from typing import Iterator, List
from .base_product import Product


class Category:
    """Базовый (родительский) класс для представления категории товаров. Список товаров является приватным атрибутом"""

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
