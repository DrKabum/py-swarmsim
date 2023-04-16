import tkinter as tk


class Upgradable:
    _level: tk.IntVar
    _name: str
    _product: str
    _level_production_multiplier: int
    _base_production: int
    _quantity: tk.IntVar
    _lore: str

    def __init__(self) -> None:
        self._quantity = tk.IntVar()
        self._level = tk.IntVar()

    @property
    def level(self) -> int:
        return self._level.get()

    @level.setter
    def level(self, value: int):
        self._level.set(value)

    @property
    def level_var(self) -> tk.IntVar:
        return self._level

    @property
    def level_production_multiplier(self) -> int:
        return self._level_production_multiplier

    @level_production_multiplier.setter
    def level_production_multiplier(self, value) -> None:
        self._level_production_multiplier = value

    @property
    def base_production(self) -> int:
        return self._base_production

    @base_production.setter
    def base_production(self, value) -> None:
        self._base_production = value

    @property
    def quantity(self) -> int:
        return self._quantity.get()

    @quantity.setter
    def quantity(self, value: int) -> None:
        self._quantity.set(value)

    @property
    def lore(self) -> str:
        return self._lore

    @lore.setter
    def lore(self, value) -> None:
        self._lore = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def product(self) -> str:
        return self._product

    @product.setter
    def product(self, value) -> None:
        self._product = value
