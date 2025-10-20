"""
Задание №4.
Реализуйте программу на Python, чтобы добавить год(-ы) к заданной дате и отобразить
новую дату.
Пример: (add_years – это имя пользовательской функции)
print(add_years(datetime.date (2015,1,1), -1))
print(add_years(datetime.date (2015,1,1), 0))
print(add_years(datetime.date (2015,1,1), 2))
print(add_years(datetime.date (2000,2,29), 1))
Output:
2014-01-01
2015-01-01
2017-01-01
2001-03-01
"""
import datetime
from datetime import timedelta


def add_years(date, shift):
    print(date + timedelta(365 * shift))


print(add_years(datetime.date(2015, 1, 1), -1))
