"""
- доработайте базовый класс `base.Vehicle`
"""

from abc import ABC, abstractmethod
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight=1.5, fuel=5, fuel_consumption=12.9):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # @abstractmethod
    def start(self) -> bool: # проверка на старт
        if not self.started:
            if self.fuel > 0:
                self.started = True
                # return self.started
            else:
                raise LowFuelError
        else:
            self.started = True
            # return self.started

    def move(self, distance):
        fuel_nes = self.fuel_consumption * abs(distance) # / 100
        if fuel_nes <= self.fuel:
            self.fuel -= fuel_nes
        else:
            raise NotEnoughFuel


# if __name__ == "__main__":
#     # test = Vehicle(10, 10, 10)
#     Vehicle.start()
#     l = test.start()
#     print(l)
#     go = test.move(-100)
#     print(go)
#     print(test.fuel)
#
#     print(test.move)