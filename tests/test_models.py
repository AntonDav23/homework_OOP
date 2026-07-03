import pytest
from src.models import Product, Category


# Тесты для класса Product
def test_product_initialization():
    """Проверяет корректность инициализации атрибутов товара."""
    sample_product = Product("Тестовый товар", "Описание товара", 1500.0, 3)

    assert sample_product.name == "Тестовый товар"
    assert sample_product.description == "Описание товара"
    assert sample_product.price == 1500.0
    assert sample_product.quantity == 3


# Тесты для класса Category
def test_category_initialization():
    """Проверяет корректность инициализации атрибутов категории."""
    prod = Product("Товар для категории", "...", 100, 1)
    category = Category("Тестовая категория", "Описание категории", [prod])

    assert category.name == "Тестовая категория"
    assert category.description == "Описание категории"
    assert len(category.products) == 1


# Тесты для подсчета (атрибутов класса)
def test_counters_with_one_category():
    """Проверяет работу счетчиков при создании одной категории."""
    Category.category_count = 0
    Category.product_count = 0

    prod1 = Product("Товар 1", "...", 100, 5)
    category = Category("Категория для теста", "...", [prod1])
