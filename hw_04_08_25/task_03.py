"""
Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e
число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……
"""

def fibonacci(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    return fibonacci(x - 2) + fibonacci(x - 1)


number = int(input("Введите число фиббоначи которое надо найти:"))

print(number, "Число Фиббоначи равно:", fibonacci(number))
