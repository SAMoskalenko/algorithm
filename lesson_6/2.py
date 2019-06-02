# Создать пользовательский класс данных (или использовать) один из классов,
# реализованных в курсе Python.Основы. Реализовать класс с применением слотов
# и обычным способом. Для объекта обычного класса проверить отображение словаря
# атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
# классов.

from pympler import asizeof


class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color


class Bike:
    __slots__ = ('name', 'speed', 'color')

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color


ferrari = Car('F40', '320 kmh', 'красный')
print(ferrari.__dict__)

ducatti = Bike('SuperSport', '300 kmh', 'красный')

print(asizeof.asizeof(ferrari))
print(asizeof.asizeof(ducatti))

# объективная реальность показывает что хранение мотоцикла Ducatti более выгодно, чем автомобиля Ferrari (272 против 536),
# однако на итоговое решение по выбору это не будет имень критическое значение