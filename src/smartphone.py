from .base_product import Product


class Smartphone(Product):
    """ Класс-наследник для смартфонов """
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        base_str = super().__str__()
        return (
            f"{base_str}\n"
            f"Характеристики: Модель {self.model}, "
            f"Память {self.memory}GB, Цвет {self.color}"
        )