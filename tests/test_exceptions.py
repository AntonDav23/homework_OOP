import pytest
from src.product import Product
from src.category import Category


def test_product_creation_with_zero_quantity():
    """Проверяет, что создание товара с 0 выбрасывает ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Product("Запрещенный товар", "Нет на складе", 100.0, 0)

    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен."


def test_category_adding_product_with_zero_quantity():
    """Проверяет, что нельзя добавить такой товар и в категорию через add_product."""
    cat = Category("Склад", "")
    with pytest.raises(ValueError):
        cat.add_product(Product("Bad", "", 10, 0))


def test_category_middle_price_normal_case():
    """ Расчет среднего ценника при наличии товаров """
    p1 = Product("A", "", 100.0, 5)
    p2 = Product("B", "", 200.0, 3)
    cat = Category("Test", "", [p1, p2])

    assert cat.middle_price() == 150.0


def test_category_middle_price_empty_list():
    """Проверка возврата 0 для пустой категории (защита от DivisionByZero)."""
    cat = Category("Пусто", "")
    assert cat.middle_price() == 0.0


def test_category_middle_price_single_item():
    """Проверка расчета, если в категории всего один товар."""
    p1 = Product("Lone Wolf", "", 999.99, 1)
    cat = Category("Одинокий", "", [p1])

    # Среднее одного числа равно самому числу
    assert cat.middle_price() == 999.99
