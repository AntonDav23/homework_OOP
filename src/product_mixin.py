from typing import Any


class CreationLoggerMixin:
    """Миксин для логирования создания объектов. Выводит в консоль имя класса и параметры инициализации"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Создан объект {self.__class__.__name__}({signature})")
        super().__init__(*args, **kwargs)
