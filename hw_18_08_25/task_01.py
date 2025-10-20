"""
Создайте класс Device, который содержит информацию об устройстве. С помощью
механизма наследования, реализуйте класс CoffeeMachine (содержит информацию
о кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder
(содержит информацию о мясорубке). Каждый из классов должен содержать необходимые
для работы методы.
"""
class Device:
    def __init__(self, typ):
        self.typ = typ

    def info(self):
        return f'Поздравляю, у вас {self.typ}'

class CoffeeMachine(Device):
    def __init__(self):
        super().__init__('Coffee Machine')

class Blender(Device):
    def __init__(self):
        super().__init__('Blender')

class MeatGrinder(Device):
    def __init__(self):
        super().__init__('Meat Grinder')

m = MeatGrinder()
print(m.info())
b = Blender()
print(b.info())
