"""
Создайте класс Circle (окружность). Для данного класса реализуйте ряд
перегруженных операторов:
Проверка на равенство радиусов двух окружностей (операция ==);
Сравнения длин двух окружностей (операции >, <, <=, >=);
Пропорциональное изменение размеров окружности, путем изменения ее радиуса
(операции +, -, +=, -=)
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other

    def __gt__(self, other):
        return self.radius > other

    def __lt__(self, other):
        return self.radius < other

    def __ge__(self, other):
        return self.radius >= other

    def __le__(self, other):
        return self.radius <= other

    def __add__(self, other):
        return f'Итоговый радиус {self.radius + other.radius}'

    def __sub__(self, other):
        return f'Итоговый радиус {self.radius + other.radius}'


c = Circle(5)
c4 = Circle(6)
print(c > c4)
print(c + c4)
print(c == c4)
