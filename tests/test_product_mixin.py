import pytest
from src.product import Product


def test_creation_logger_mixin_output(capsys):
    """ Проверяет, что миксин выводит информацию о создании объекта в консоль """
    prod = Product("Книга", "Тест", 500, 10)

    captured = capsys.readouterr()

    # Проверяем наличие строки в консоли
    assert "Создан объект Product(" in captured.out
    assert "'Книга'" in captured.out
    assert "500" in captured.out
    assert "10" in captured.out