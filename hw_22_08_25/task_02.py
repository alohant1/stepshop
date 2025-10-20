from random import randint
from enum import Enum
from time import sleep

class Game(Enum):
    Rock = 1
    Scissors = 2
    Paper = 3

    def start(self):
        print("Выбирай свою судьбу из:\n"
            "1) Камень   2) Ножницы   3) Бумага   4) Выйти")
        inpu = int(input('>>> '))
        if inpu == 1 or 2 or 3:
            self.play(self, inpu)
        elif inpu == 4:
            exit()
        else:
            print("Неверный ввод")


    def play(self, choice):
        pc = randint(1, 3)
        print(f'Вы выбрали {Game(choice).name}')
        if pc == choice:
            print(f'Draw, both chose {Game(choice).name}\n')
        elif choice - pc == 1:
            print(f'Вы проиграли, {Game(choice).name} < {Game(pc).name}')
        elif pc - choice == 1:
            print(f'Вы выиграли, {Game(choice).name} > {Game(pc).name}')
        elif pc == 3 and choice == 1:
            print(f'Вы проиграли, {Game(choice).name} < {Game(pc).name}')
        elif pc == 1 and choice == 3:
            print(f'Вы выиграли, {Game(choice).name} > {Game(pc).name}')
        self.game_end(self)

    def game_end(self):
        sleep(0.5)
        en = int(input('Чтобы сыграть снова нажмите 1, для прекращения, нажмите 2\n>>> '))
        if en == 1:
            self.start(self)
        else:
            exit()


g = Game
Game.start(g)
