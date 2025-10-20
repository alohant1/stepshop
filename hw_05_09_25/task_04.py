"""
4. Написать функцию-генератор с yield, которая может перебирать числа, делящиеся
на 7, в диапазоне от 0 до n.
"""
def yielding(n):
    for i in range(0, n):
        if i % 7 == 0:
            yield i

for x in yielding(39):
    print(x)
