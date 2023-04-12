"""
создайте класс `Car`, наследник `Vehicle`
- в модуле `car` создайте класс `Car`
    - класс `Car` должен быть наследником `Vehicle`
    - добавьте атрибут `engine` классу `Car`
    - объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(self, eng):
        self.engine = eng


car_1 = Car(10, 5, 6)
eng_1 = Engine(3, 9)
car_1_engine = car_1.set_engine(eng_1)
print(car_1_engine)
# print(Engine)



