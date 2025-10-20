"""
Создайте класс Complex (комплексное число).
Создайте перегруженные операторы для реализации арифметических операций
по работе с комплексными числами (операции +, -, *, /).
"""
class Complex:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

a = Complex(12)
b = Complex(15)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
