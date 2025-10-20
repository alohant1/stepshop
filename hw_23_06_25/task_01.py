"""
Есть кортеж с названиями производителей автомобилей (название производителя
может встречаться от 0 до N раз). Пользователь вводит с клавиатуры название производителя
и слово для замены. Необходимо заменить в кортеже все элементы с этим названием на слово
для замены. Совпадение по названию должно быть полным.
"""

cars = ('Mercedes', 'Toyota', 'Mercedes', 'DHL', 'Mercedes', 'Toyota')
cars_changeable = list(cars[:])

change_from = input('Введите производителя авто для замены\n>>>')
change_to = input('Введите на что заменить производителя\n>>>')


if change_from in cars_changeable:
    for cars_changeable in cars_changeable:
        index_of_change_from = int(cars_changeable.index(change_from))
        cars_changeable[index_of_change_from] = change_to
    print(cars_changeable)
else:
    print("Такого нет в списке")
