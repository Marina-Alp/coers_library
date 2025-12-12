class Book:
    '''
    Класс создания и взаимодействия с книгой
    '''
    def __init__(self, name, author, year):
        """
        Базовый конструктор класса
        :param name: Название книги
        :param author: Имя автора книги
        :param year: Год выпуска книги
        """
        self._name = name
        self._author = author
        self._year = year

    @property
    def full_name_book(self):
        """
        Метод обращения к книги
        :return: Полное наименования книги
        """
        return self._name + " , " + self._author + " , " + str(self._year)

    @full_name_book.setter
    def full_name_book(self, new):
        """
        Метод меняет исходно введённые параметры книги
        :param new: 'Название книги, имя автора книги, год выпуска книги'
        :return: Новые значения : названия, имени автора, года выпуска
        """
        if new is not None:
            self._name, self._author, self._year = new.replace(' ','').split(",")
        else: self._name, self._author, self._year = 'Этой, книги, нет'.split(",")


    @full_name_book.deleter
    def full_name_book(self):
        """
        Метод удаляет книгу
        :return: None
        """
        print(f"{self} - удалина")
        self.full_name_book = None


    def __str__(self): #__str__?
        """
        Выводит полное имя книги
        :return: f'Это книга: "{Полное имя книги}"'
        """
        return f'Это книга: "{self.full_name_book}"'

    def compare(self, compare_book):
        """
        Метод сравнения двух книг
        :param compare_book: Полное имя книги с которой сравнивают
        :return: True/False
        """
        if self.full_name_book == compare_book:
            print("Книги одинаковы")
            return True
        else:
            print("Книги разные")
            return False
