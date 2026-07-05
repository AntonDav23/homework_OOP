import pytest
from src.models import Product, Category, CategoryIterator

# Тесты для класса Product
def test_product_initialization():
    """
    Проверяет, что объект Product корректно инициализируется
    с правильными значениями атрибутов name, description, price и quantity.
    """
    sample_product = Product("Тестовый товар", "Описание товара", 1500.0, 3)

    assert sample_product.name == "Тестовый товар"
    assert sample_product.description == "Описание товара"
    assert sample_product.price == 1500.0
    assert sample_product.quantity == 3


def test_product_price_setter_valid():
    """
    Проверяет, что сеттер цены корректно обновляет приватный атрибут __price,
    если передано положительное значение.
    """
    product = Product("Товар", "...", 100, 5)
    product.price = 200.0

    assert product.price == 200.0


def test_product_price_setter_invalid():
    """
    Проверяет, что сеттер цены не обновляет атрибут и выводит предупреждение в консоль,
    если передано нулевое или отрицательное значение.
    """
    product = Product("Товар", "...", 100, 5)

    product.price = -50.0

    assert product.price == 100.0


def test_product_new_product_classmethod():
    """
    Проверяет, что класс-метод new_product() корректно создает и возвращает
    экземпляр класса Product на основе данных из словаря.
    """
    data = {
        "name": "Созданный из словаря",
        "description": "Новый товар",
        "price": 999.99,
        "quantity": 10
    }
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Созданный из словаря"
    assert product.price == 999.99


def test_product_str_representation():
    """Проверяет строковое отображение объекта Product через __str__."""
    product = Product("Смартфон", "Новый флагман", 99999.0, 5)
    expected_str = "Смартфон, 99999.0 руб. Остаток: 5 шт."
    assert str(product) == expected_str


def test_product_addition():
    """Проверяет логику сложения двух товаров (__add__) для получения общей стоимости."""
    a = Product("Товар А", "", 100.0, 10)  # Стоимость склада: 100 * 10 = 1000
    b = Product("Товар Б", "", 200.0, 2)  # Стоимость склада: 200 * 2 = 400

    result = a + b
    expected_total = 1400.0

    assert result == expected_total
    assert isinstance(result, float)


# Тесты для класса Category
def test_category_initialization():
    """
    Проверяет корректность инициализации объекта Category.
    Также проверяет, что геттер products возвращает строку с информацией о товарах.
    """
    prod = Product("Товар для категории", "...", 100, 1)
    category = Category("Тестовая категория", "Описание категории", [prod])

    assert category.name == "Тестовая категория"
    assert category.description == "Описание категории"

    result_str = category.products
    assert isinstance(result_str, str)
    assert "Товар для категории" in result_str


def test_category_add_product():
    """Проверяет метод add_product() и обновление глобальных счетчиков класса"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая категория", "")
    assert len(category._product_list) == 0

    new_prod = Product("Новый товар", "...", 500, 1)
    category.add_product(new_prod)

    assert len(category._product_list) == 1
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_str_representation():
    """Проверяет строковое отображение объекта Category через __str__."""
    p1 = Product("A", "", 10, 2)  # Количество: 2
    p2 = Product("B", "", 20, 3)  # Количество: 3
    Category.category_count = 0  # Сброс для чистоты теста
    category = Category("Электроника", "", [p1, p2])

    expected_str = "Электроника, количество продуктов: 5 шт."
    assert str(category) == expected_str


def test_category_iterator():
    """Проверяет работу класса-итератора CategoryIterator. Проверяет методы __iter__ и __next__"""
    p1 = Product("Книга 1", "", 500, 1)
    p2 = Product("Книга 2", "", 600, 1)
    p3 = Product("Книга 3", "", 700, 1)

    category = Category("Книги", "", [p1, p2, p3])

    iterator = CategoryIterator(category)

    collected_products = list(iterator)

    assert len(collected_products) == 3
    assert collected_products[0].name == "Книга 1"
    assert collected_products[1].name == "Книга 2"
    assert collected_products[2].name == "Книга 3"


def test_for_loop_iteration_over_category():
    """Проверяет возможность использования итератора в цикле for напрямую"""
    p1 = Product("Монитор", "", 15000, 2)
    p2 = Product("Мышь", "", 2000, 5)

    category = Category("Периферия", "", [p1, p2])

    names_in_loop = []
    for product in CategoryIterator(category):
        names_in_loop.append(product.name)

    assert names_in_loop == ["Монитор", "Мышь"]
