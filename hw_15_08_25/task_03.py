"""
Вам необходимо создать класс Airplane (самолет).
С помощью перегрузки операторов реализовать:
Проверка на равенство типов самолетов (операция ==);
Увеличение и уменьшение пассажиров в салоне самолета (операции +, -, +=, -=);
Сравнение двух самолетов по максимально возможному количеству пассажиров
на борту (операции >, <, <=, >=).
"""
class Airplane:
    def __init__(self, typ, passengers, max_pass):
        self.typ = typ
        self.passengers = passengers
        self.max_pass = max_pass

    def __eq__(self, other):
        return self.typ == other.typ

    def __add__(self, other):
        res = self.passengers + other
        if res <= 0:
            return f'Самолёт пуст, 0 пассажиров'
        elif res >= self.max_pass:
            return f'{self.max_pass}, самолёт переполнен'
        return res


    def __sub__(self, other):
        res = self.passengers - other
        if res <= 0:
            return f'Самолёт пуст, 0 пассажиров'
        elif res >= self.max_pass:
            return f'{self.max_pass}, самолёт переполнен'
        return res

    def __gt__(self, other):
        return self.max_pass > other.max_pass

    def __lt__(self, other):
        return self.max_pass < other.max_pass

    def __ge__(self, other):
        return self.max_pass >= other.max_pass

    def __le__(self, other):
        return self.max_pass <= other.max_pass


air_01 = Airplane('Toyota', 50, 150)
air_02 = Airplane('Toyota', 100, 282)
print(air_01 == air_02)
print(air_01 + 1000)
print(air_01 < air_02)
