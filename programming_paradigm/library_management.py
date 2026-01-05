class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self.__is_checked_out = _is_checked_out

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        return [book.title for book in self._books if book.is_available()]
