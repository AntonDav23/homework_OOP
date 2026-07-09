import pytest
from src import Product


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
