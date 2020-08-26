from datetime import datetime


class CountPagesException(Exception):
    def __init__(self, message):
        super().__init__(message)


class YearException(Exception):
    def __init__(self, message):
        super().__init__(message)


class AuthorException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PriceException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Book:
    count_pages: int
    year: int
    author: str
    price: int

    def __init__(self, count_pages: int, year: int, author: str, price: int):
        ### validate dat
        self.count_pages = count_pages
        self.year = year
        self.__author = author
        self.__price = price

    @property
    def count_pages(self):
        return self.__count_pages

    @property
    def year(self):
        return self.__year

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @count_pages.setter
    def count_pages(self, count_pages):
        if count_pages > 0 and type(count_pages) == int:
            self.__count_pages = count_pages
        else:
            raise CountPagesException('invalid count pages')

    @year.setter
    def year(self, year):
        if year in range(datetime.now().year):
            self.__year = year
        else:
            raise YearException('invalid year')

    @author.setter
    def author(self, author):
        if type(author) == str:
            self.__author = author
        else:
            raise AuthorException('invalid author')

    @price.setter 
    def price(self, price):
        if type(price) is int and price >= 0:
            self.__price = price
        else:
            raise PriceException('invalid price') 
        
        
if __name__ == '__main__':
    b = Book(100, 2010, 'roma', 4)
