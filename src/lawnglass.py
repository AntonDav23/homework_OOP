from .product import Product


class LawnGrass(Product):
    """Класс-наследник для газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}\n" f"Характеристики: Страна {self.country}, " f"Прорастание {self.germination_period} дней"
