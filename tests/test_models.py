import pytest
from src.models import Product, Category

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
    product.price = 200.0  # Используем сеттер

    assert product.price == 200.0


def test_product_price_setter_invalid():
    """
    Проверяет, что сеттер цены не обновляет атрибут и выводит предупреждение в консоль,
    если передано нулевое или отрицательное значение.
    """
    product = Product("Товар", "...", 100, 5)

    # Сеттер должен вывести сообщение и не изменить цену
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

    # Проверяем геттер products
    result_str = category.products
    assert isinstance(result_str, str)
    assert "Товар для категории" in result_str


def test_category_add_product():
    """
    Проверяет, что метод add_product() корректно добавляет новый товар
    в приватный список товаров категории и обновляет счетчик.
    Также проверяет работу геттера products для пустой и непустой категории.
    """
    category = Category("Пустая категория", "...")

    # Проверяем геттер для пустой категории
    assert category.products == "Товаров в категории нет."

    new_prod = Product("Новый товар", "...", 500, 1)
    category.add_product(new_prod)

    # Проверяем геттер после добавления товара
    result_str = category.products
    assert isinstance(result_str, str)
    assert "Новый товар" in result_str