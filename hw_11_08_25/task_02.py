"""
Задание №2
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год
выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода
данных, реализуйте доступ к отдельным полям через методы класса.
"""

class Book:

    def __init__(self, name, release_year, publisher, genre, author, price):
        self.__name = name
        self.__release_year = release_year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    #Название
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nam):
        self.__name = nam

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

    #Издатель
    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publish):
        self.__publisher = publish

    #Жанр
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genr):
        self.__genre = genr

    #Автор
    @property
    def author(self):
       return self.__author

    @author.setter
    def author(self, autho):
        self.__author = autho

    #Цена
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,pric):
        self.__price = pric


c = Book("War and peace", "1906", "New Blood", "Novel", "Dostoevski", "15_000")
print(c.name)
c.release_year = 1907
c.author = "Dostal"
c.price = 17_000
print(c.publisher, c.author)

