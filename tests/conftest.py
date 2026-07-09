import pytest
from src.category import Category

@pytest.fixture(autouse=True)
def reset_global_counters():
    """
    Сбрасывает глобальные счетчики перед каждым тестом в проекте,
    чтобы обеспечить полную изоляцию тестов друг от друга.
    """
    initial_cat_count = Category.category_count
    initial_prod_count = Category.product_count

    yield

    Category.category_count = initial_cat_count
    Category.product_count = initial_prod_count