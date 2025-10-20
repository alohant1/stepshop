"""
Реализуйте программу, чтобы найти дату понедельника данной недели.
Date: 2015 50
Output: пн 14 декабря 00:00:00 2015
"""
import datetime
from datetime import timedelta

year_week = list(map(int, input('Введите неделю и год: ').split()))
year = year_week[0]
week_num = year_week[1]
ik = datetime.date(year, 1, 1).isocalendar()[2]
i = 0

for i in range(9):
    if ik == 8 or ik == 1:
        break
    ik += 1
    i += 1

ik = datetime.date(year, 1, i)

for b in range(0, week_num - 1):
    ik += timedelta(weeks=1)

print(ik + timedelta(days=1))
