"""
Задание №1
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы
класса.
"""

class Cars:

    def __init__(self, model, release_year, creator, engine_volume, colour, price):
        self.__model = model
        self.__release_year = release_year
        self.__creator = creator
        self.__engine_volume = engine_volume
        self.__colour = colour
        self.__price = price
    # Модель
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, mod):
        self.__model = mod
    # год выхода
    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, release):
        if release < 2010:
            self.__release_year = 2010
        else:
            self.__release_year = release
    #Производитель
    @property
    def creator(self):
        return self.__creator

    @creator.setter
    def creator(self, creat):
        self.__creator = creat
    #Обьём
    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, volume):
        self.__engine_volume = volume
    #Цвет и цена не меняются
    def colour(self):
       return self.__colour

    def price(self):
        return self.__price


c = Cars("Volvo", "2006", "Person", "2000", "Yellow", "15_000_000")
print(c.model)
c.release_year = 2000
c.creator = "Toyota"
c.engine_volume = 100
print(c.engine_volume, c.model)

