from typing import Iterator, List

from src.product import Product


class Category:
    """Класс для представления категории товаров в магазине"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product] | None = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []
        Category.category_count += 1
        if products is not None:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию после проверки его типа"""
        if not isinstance(product, Product):
            raise TypeError(f"В категорию можно добавлять только объекты Product, получено: {type(product).__name__}")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Публичный геттер для получения списка товаров"""
        return self.__products.copy()

    @property
    def products_info(self) -> str:
        """Возвращает отформатированную строку со всеми товарами в категории"""
        if not self.__products:
            return "Товаров в категории нет."

        lines = [str(product) for product in self.__products]
        return "\n".join(lines)

    @property
    def _product_list(self) -> List[Product]:
        """Защищенный геттер для внутреннего использования"""
        return self.__products

    def __str__(self) -> str:
        """Возвращает строковое представление категории"""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self) -> float:
        """Рассчитывает среднюю цену одного товара в категории"""
        try:
            total_sum = sum(product.price for product in self.__products)
            count = len(self.__products)
            return total_sum / count

        except ZeroDivisionError:
            return 0.0


class CategoryIterator(Iterator):
    """Вспомогательный класс-итератор для безопасного перебора товаров категории"""

    def __init__(self, category: Category):
        self._items = category._product_list
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration
