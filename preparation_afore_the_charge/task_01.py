from collections import Counter

order = list()
payment_complete = False

def create_order():
    print('Меню: 1) Пепперони    2) Барбекю    3) Дары Моря\n'
          'Для информации о пицце введите 4, для продолжения введите 5')
    while 1 == True:
        ad = (input('Введите номер выбранного вами действия: '))
        if ad == '4':
            Pizza.info_menu()
        elif ad == '1':
            order.append("Пепперони")
        elif ad == '2':
            order.append("Барбекю")
        elif ad == '3':
            order.append("Дары моря")
        elif ad == '5':
            Pizza.payment()
        else:
            print('Неверно введённая команда')
        print(f'Ваш заказ: {Counter(order)}')


class Pizza:
    _pizza = 0
    @staticmethod
    def info_menu():
        print('1) Пепперони    2) Барбекю    3) Дары Моря   4) Вернуться к заказу')
        infoed = input('О чём вы хотите узнать информацию: ')
        if infoed == '1':
            print(Pepperoni.stuff())
        if infoed == '2':
            print(Barbeque.stuff())
        if infoed == '3':
            print(SeaGifts.stuff())


    def info(self):
        print(f"Название: {self.__class__.__name__}\n",
              self.stuff)

    @staticmethod
    def stuff():
        return None

    @staticmethod
    def payment():
        orde = dict(Counter(order))
        if orde.get('Пепперони') is None:
            pep_sum = 0
        else:
            pep_sum = 100 * orde['Пепперони']

        if orde.get('Барбекю') is None:
            bar_sum = 0
        else:
            bar_sum = 500 * orde['Барбекю']

        if orde.get('Дары моря') is None:
            sea_sum = 0
        else:
            sea_sum = 300 * orde['Дары моря']
        totale = pep_sum + bar_sum + sea_sum
        print(f'Ваш итог к оплате: {totale}\n'
              'Для отмены заказа введите 14884206978412654784621784214214124257954'
              'Для продолжения оплаты введите вашу сумму ниже')
        pay = int(input('>>> '))
        if pay == '14884206978412654784621784214214124257954':
            print('Заказ отменён')
            order.clear()
        elif pay == totale:
            print('Оплата успешно завершена, приятного аппетита!')
            exit()
        else:
            print('Вы ввели неверное значение\n')


class Pepperoni(Pizza):
    @staticmethod
    def stuff():
        return ("Тесто: 1 тип\n"
               "Соус: 1 тип\n"
               "Начинка: 1 тип\n"
                "Стоимость: 100 нервных клеток\n")

class Barbeque(Pizza):
    @staticmethod
    def stuff():
        return ("Тесто: 2 тип\n"
               "Соус: 2 тип\n"
               "Начинка: 2 тип\n"
                "Стоимость: 500 нервных клеток\n")

class SeaGifts(Pizza):
    @staticmethod
    def stuff():
        return ("Тесто: 3 тип\n"
               "Соус: 3 тип\n"
               "Начинка: 3 тип\n"
                "Стоимость: 300 нервных клеток\n")

create_order()
