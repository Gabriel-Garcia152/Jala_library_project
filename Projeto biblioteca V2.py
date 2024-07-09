class Book:
    def __init__(self, title, author, release_date, topic):
        self.title = title
        self.author = author
        self.release_date = release_date
        self.topic = topic

class Catalog:
    def __init__(self):
        self.book_list = []

    def show_catalog(self):
        for book in self.book_list:
            print(f'''
                    Título: {book.title}
                    Autor: {book.author}
                    Data de Lançamento: {book.release_date}
                    Tópico: {book.topic}
                ''')

    def search_by_topic(self, topic):
        found_books = []

        for book in self.book_list:
            if book.topic == topic:
                found_books.append(book)

        if found_books:
            return found_books
        else:
            return "Tópico não encontrado"

    def show_by_topic(self, topic):
        found_books = self.search_by_topic(topic)
        for book in found_books:
            print(f'''
                    Título: {book.title}
                    Autor: {book.author}
                    Data de Lançamento: {book.release_date}
                    Tópico: {book.topic}
                ''')

    def search_book(self, title):
        for book in self.book_list:
            if book.title == title:
                return book
    
    def show_book(self, title):
        book = self.search_book(title)
        print(f'''
                    Título: {book.title}
                    Autor: {book.author}
                    Data de Lançamento: {book.release_date}
                    Tópico: {book.topic}
                ''')

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, title):
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)

library = Catalog()
book_1 = Book("ABC", "ABC", 2020, "Programming")
book_2 = Book("XYZ", "XYZ", 2015, "Programming")

library.add_book(book_1)
library.add_book(book_2)
library.show_catalog()
library.show_by_topic("Programming")
library.show_book("ABC")
library.remove_book("ABC")
library.show_catalog()
