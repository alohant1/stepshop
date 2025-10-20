"""
Есть кортеж с названиями производителей автомобилей (название производителя
может встречаться от 0 до N раз). Пользователь вводит с клавиатуры название производителя
и слово для замены. Необходимо заменить в кортеже все элементы с этим названием на слово
для замены. Совпадение по названию должно быть полным.
"""

manufacturers = tuple(["Toyota", 'Mercedes', 'Mercedes', 'DHL'])

finding = input("Введите производителя машины для замены:")
replcement = input("Введите то, на что заменить производителя:")

for manufacturers in manufacturers:
    manuf_index = manufacturers.index(finding)
    manuf_index = int(manuf_index)
    manufacturers[manuf_index] = replcement

print(manufacturers)
