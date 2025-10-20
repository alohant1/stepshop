"""
Напишите программу, в которой я ввожу целые числа a, b, c. Если существует треугольник
со сторонами a, b, c, то программа выведет true, иначе false.
Ввод:    Ввод:
6 7 8    2 3 6
Вывод:    Вывод:
true    false
"""

a, b, c = map(int, input("Введите 3 стороны треугольника\n >>>").split())
print(a / b)

if a < b + c and b < a + c and c < a + b:
    print(True)
else:
    print(False)
