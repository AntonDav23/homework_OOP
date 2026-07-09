import pytest
from src.smartphone import Smartphone


def test_smartphone_inheritance_and_attributes():
    """Проверяет создание Смартфона и наличие специфичных атрибутов"""
    phone = Smartphone(
        name="Galaxy",
        description="S24",
        price=120000.0,
        quantity=5,
        efficiency="Snapdragon",
        model="SM-S928B",
        memory=512,
        color="Бежевый"
    )

    assert isinstance(phone, object)

    assert phone.efficiency == "Snapdragon"
    assert phone.model == "SM-S928B"
    assert phone.memory == 512
    assert phone.color == "Бежевый"


def test_smartphone_str_representation():
    """Проверяет формат строки __str__ для смартфона"""
    phone = Smartphone("Test", "T", 1, 1, "E", "M", 64, "C")
    result = str(phone)

    assert "Test, 1 руб." in result
    assert "Память 64GB" in result
    assert "Цвет C" in result