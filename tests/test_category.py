import pytest
from src.category import Category, CategoryIterator
from src.smartphone import Smartphone
from src.lawnglass import LawnGrass


def test_category_add_valid_products():
    """Проверяет добавление валидных продуктов (Product и его наследников)"""
    cat = Category("Электроника", "")

    phone = Smartphone("S", "", 100, 1, "", "", 0, "")
    grass = LawnGrass("G", "", 50, 10, "", 0, "")

    cat.add_product(phone)
    cat.add_product(grass)

    assert len(cat._product_list) == 2
    assert Category.product_count == 2


def test_category_str_representation_calculates_quantity():
    """Проверяет подсчет общего количества (quantity) в методе __str__."""
    p1 = Smartphone("S1", "", 100, 2, "", "", 0, "")  # qty 2
    p2 = LawnGrass("G1", "", 50, 5, "", 0, "")  # qty 5

    cat = Category("Все товары", "", [p1, p2])

    expected_str = "Все товары, количество продуктов: 7 шт."
    assert str(cat) == expected_str


def test_category_iterator_functionality():
    """Проверяет работу вспомогательного класса-итератора."""
    items = [
        Smartphone("P1", "", 1, 1, "", "", 0, ""),
        LawnGrass("P2", "", 1, 1, "", 0, "")
    ]
    cat = Category("Iter Test", "", items)

    iterator = CategoryIterator(cat)
    collected = list(iterator)

    assert len(collected) == 2
    assert collected[0].name == "P1"
    assert collected[1].name == "P2"