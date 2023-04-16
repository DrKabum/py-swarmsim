import math, time, yaml
import tkinter as tk
from classes.upgradable import Upgradable


class Game:
    _tick_wait_time: int
    _meat_quantity: float
    _upgradables: list[Upgradable]
    _is_game_on: bool
    _last_tick_time: int | None
    _window: tk.Tk

    def __init__(self, window: tk.Tk, tick_wait_time: int, starting_meat: int) -> None:
        self._window = window
        self._tick_wait_time = tick_wait_time
        self._meat_quantity = starting_meat
        self._meat = tk.IntVar(value=starting_meat)
        self._upgradables = self._get_upgradables()
        self.add("drone", 1)
        self.tick()

    @property
    def tick_wait_time(self):
        return self._tick_wait_time

    @tick_wait_time.setter
    def tick_wait_time(self, value: int):
        self._tick_wait_time = value

    @property
    def meat(self):
        return self._meat.get()

    @meat.setter
    def meat(self, value: int | float):
        self._meat.set(math.trunc(value))

    @property
    def meat_var(self) -> tk.IntVar:
        return self._meat

    @property
    def meat_quantity(self) -> float:
        return self._meat_quantity

    @meat_quantity.setter
    def meat_quantity(self, value: float):
        self._meat_quantity = value

    @property
    def is_game_on(self):
        return self._is_game_on

    @is_game_on.setter
    def is_game_on(self, value: bool):
        self._is_game_on = value

    @property
    def upgradables(self):
        return self._upgradables

    def _get_upgradables(self) -> list[Upgradable]:
        output = []

        with open("classes/game-data.yaml", "r") as config:
            data = yaml.safe_load(config)

        for creature in data["creatures"]:
            new_creature = Upgradable()
            new_creature.name = creature["name"]
            new_creature.level_production_multiplier = creature["level-production-multiplier"]
            new_creature.lore = creature["lore"]
            new_creature.base_production = creature["base-production"]
            new_creature.product = creature["product"]
            output.append(new_creature)

        return output

    def tick(self):
        for upgradable in self._upgradables:
            if upgradable.product == "meat":
                self._meat_quantity += upgradable.base_production * upgradable.quantity
                self.meat = self._meat_quantity
                continue

        self._window.after(self.tick_wait_time, self.tick)

    def get(self, upgradable_name: str) -> Upgradable:
        up = list(filter(lambda u: u.name == upgradable_name, self._upgradables))

        if len(up) == 0:
            raise Exception(f"{upgradable_name} is not a valid upgradable.")

        return up[0]

    def add(self, upgradable_name: str, quantity: int):
        up = self.get(upgradable_name)
        up.quantity += quantity

    def get_timestamp(self):
        return math.trunc(time.time_ns() / 1000000)
