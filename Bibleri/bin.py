from book import Book

if __name__ == '__main__':
    kak = Book('kjhg','jhgf',2012)
    print(kak)
    kak.full_name_book = 'kur, iuhn, 2000'
    print(kak)
    eto = Book("fyj", "djh?", 2510)
    print(kak.compare(eto))
    del kak.full_name_book
    print(kak)
