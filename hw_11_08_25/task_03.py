"""
Задание №3
Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
вывода данных, реализуйте доступ к отдельным полям через методы класса.
"""

class Stadium:

    def __init__(self, name, opening_year, country, city, capacity):
        self.__name = name
        self.__opening_year = opening_year
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    #Название
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nam):
        self.__name = nam

    #Год открытия
    @property
    def opening_year(self):
        return self.__opening_year

    @opening_year.setter
    def opening_year(self, opened):
        if opened < 2010:
            self.__opening_year = 2010
        else:
            self.__opening_year = opened

    #Страна
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, countr):
        self.__country = countr

    #Город
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, cit):
        self.__city = cit

    #Вместимость
    @property
    def capacity(self):
       return self.__capacity

    @capacity.setter
    def capacity(self, capac):
        self.__capacity = capac



c = Stadium("Almaty Grand Stadium", "1938", "Idk", "Almaty", 20000)
print(c.name)
c.opening_year_year = 1947
c.country = "Kazakhstan"

print(c.country, c.city)
print(c.capacity)
