"""
Создайте класс Roman (РимскоеЧисло), представляющий римское число
и поддерживающий операции +, -, *, /.
При реализации класса:
• операции +, -, *, / реализуйте как специальные методы
• методы преобразования как статические методы.
"""
from collections import Counter

class RomanNumerals:

    @staticmethod
    def conversion_unto_roman(cls):
        counts = dict(Counter(cls.upper()))
        #Для рассчёта сколько римских единиц в числе и что с ними делать
        if counts.get('I') is not None:
            if cls[0] and cls[-1] == 'I':
                number = counts['I']
            elif cls[0] == 'I':
                number = -counts['I']
            elif cls[-1] == 'I':
                number = counts['I']
            elif cls[-1] == 'V' or 'X' or 'L':
                number = -counts['I']
            else:
                number = 0
        else:
            number = 0

        if counts.get('V') is None:
            v_num = 0
        else:
            v_num = 5 * counts['V']

        if counts.get('X') is None:
            x_num = 0
        else:
            x_num = 10 * counts['X']

        if counts.get('L') is None:
            l_num = 0
        else:
            l_num = 50 * counts['L']

        # Неправильную запись римских чисел к сожалению не исправляет
        summ = number + v_num + x_num + l_num
        return summ


RomanNumerals.conversion_unto_roman('XXXIX')
