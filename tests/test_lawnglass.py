import pytest
from src.lawnglass import LawnGrass


def test_lawnglass_inheritance_and_attributes():
    """Проверяет создание Газонной травы и наличие специфичных атрибутов"""
    grass = LawnGrass(
        name="Рулонный",
        description="Премиум",
        price=800.0,
        quantity=20,
        country="Россия",
        germination_period=7,
        color="Изумрудный"
    )

    assert hasattr(grass, 'country')
    assert hasattr(grass, 'germination_period')

    assert grass.country == "Россия"
    assert grass.germination_period == 7
    assert grass.color == "Изумрудный"


def test_lawngrass_str_representation():
    """Проверяет формат строки __str__ для газона"""
    grass = LawnGrass("G", "D", 10, 5, "RU", 10, "Green")
    result = str(grass)

    assert "G, 10 руб." in result
    assert "Страна RU" in result
    assert "Прорастание 10 дней" in result