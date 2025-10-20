"""
Напишите функцию, которая проверяет является ли число степенью двойки. Если
истинно выведите True, иначе False.
Input
8
Output
True
"""

def sq_root(num):
    a = 2
    if num == 2:
        return True
    elif num == 1:
        return True
    for i in range(num // 4):
        a *= 2
        if a == num:
            return True
    return False


print(sq_root(8))
