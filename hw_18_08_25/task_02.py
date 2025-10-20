"""
Создайте класс Ship, который содержит информацию о корабле. С помощью
механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате),
класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию
о крейсере). Каждый из классов должен содержать необходимые для работы методы.
"""
class Ship:
    def __init__(self, typ):
        self.typ = typ

    def info(self):
        return f'Поздравляю, у вас {self.typ}'

    @staticmethod
    def more_info(self):
        return None

class Frigate(Ship):
    def __init__(self):
        super().__init__('Frigate')

    def more_info(self):
        return 'Фрегаты - боевые корабли среднего водоизмещения океанской зоны, обладающие универсальным ракетно-артиллерийским вооружением.'

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destroyer')

    def more_info(self):
        return 'Эскадренный миноносец (эсминец) — класс многоцелевых боевых быстроходных манёвренных кораблей.'

class Cruiser(Ship):
    def __init__(self):
        super().__init__('Cruiser')

    def more_info(self):
        return 'Крейсер — класс боевых надводных кораблей, способных выполнять задачи независимо от основного флота. '

d = Destroyer()
print(d.info(), d.more_info())
