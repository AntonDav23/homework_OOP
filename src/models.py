from typing import List


class Product:
    """
    Класс для представления товара.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.
    Содержит счетчики общего количества категорий и товаров.
    """
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий
        Category.category_count += 1
        # Увеличиваем счетчик товаров на количество товаров в новой категории
        Category.product_count += len(self.products)
