from book import Book

class Library:
    def __init__(self, list_books=None):
        if list_books is None:
            list_books = []
        self.__list_books = list_books

    @property
    def library(self):
        return self.__list_books

    @library.setter
    def library(self, changes, plus_or_minus=None):
        if plus_or_minus == None:
            plus_or_minus = True
        if plus_or_minus == True:
            return self.library.append(changes)
        else:
            if changes in self.library:
                self.library.pop(changes)
                return self.library
            else:
                print(f'Книги "{changes}" в библиотеке нет')
                return self.library
