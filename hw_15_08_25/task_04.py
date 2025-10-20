"""
Создать класс Flat (квартира). Реализовать перегруженные операторы:
Проверка на равенство площадей квартир (операция ==);
Проверка на неравенство площадей квартир (операция !=);
Сравнение двух квартир по цене (операции >, <, <=, >=).
"""
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


fl_01 = Flat(101, 250_000_000_000)
fl_02 = Flat(1205, 250_000_000_000_0)
fl_03 = Flat(10, 250_000_000)
print(fl_01 != fl_02)
print(fl_03 > fl_02)
print(fl_01 <= fl_03)
