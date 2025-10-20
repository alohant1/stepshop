"""
Задание №1.
Реализуйте программу, для получения номера недели.
Date: 2015 6 16
Output: 25
"""
import datetime

date = datetime.date(2015, 6, 16)
week_num = date.isocalendar()[1]
print(week_num)

