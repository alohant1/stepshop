"""
Напишите программу для создания списка, длина которого равна N. После создания
списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных,
вывод должен быть «Нет», в остальных ключах «Да».
"""

import random

i = 0
amount = int(input("Введите сколько чисел сгенерировать\n>>>"))
nums = []

while i != amount:
    nums.append(random.randint(1, 1000))
    i += 1


print("Вот список чисел: ", nums, end='\n\n')
chet = list(filter(lambda n: n%2 == 0, nums))
nechet = list(filter(lambda n: n%2 == 1, nums))

print("Чётные числа:", chet)
print("Нечётные числа:", nechet)
if len(chet) > len(nechet):
    print("Чётных чисел больше")
elif len(nechet) > len(chet):
    print("Нечётных чисел больше")
else:
    print("Идеальный баланс")

