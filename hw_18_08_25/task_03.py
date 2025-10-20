"""
Используя механизм множественного наследования разработайте класс «Автомобиль».
Должны быть классы «Колеса», «Двигатель», «Двери».
"""
class Wheel:

    def wheel(self):
        return 'I am spinning'

class Engine:

    def engine(self):
        return 'Vroom-vroom'

class Doors:

    def doors(self):
        return '*Вставьте сюда скрип двери*'


class Car(Wheel, Engine, Doors):
    pass

c = Car()
print(c.wheel())
print(c.engine())
print(c.doors())
