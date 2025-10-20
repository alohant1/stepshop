"""
Задание №3.
Реализуйте программу, чтобы выбрать все воскресенья определенного года.
"""
import datetime
from datetime import timedelta


y = int( input('Введите год: '))
year = y
ik = datetime.date(year, 1, 1).isocalendar()[2]
print(year)
i = 0

for i in range(9):
    i += 1
    if ik == 7:
        print(ik)
        break
    ik += 1

all_sundays_lst = []
ik = datetime.date(year, 1, i) - timedelta(days=1)
for d in range(52):
    print(ik)
    all_sundays_lst.append(ik)
    ik += timedelta(days=7)
