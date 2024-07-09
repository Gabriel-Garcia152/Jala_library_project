class Catalog:
    def __init__(self):
        self.book_list = []

    def show_catalog(self):
        for book in self.book_list:
            self.format_book_data(book)

    def search_by_topic(self, topic):
        found_books = []

        for book in self.book_list:
            if book.topic == topic:
                found_books.append(book)

        if found_books:
            return found_books
        else:
            return "Tópico não encontrado!"

    def show_by_topic(self, topic):
        found_books = self.search_by_topic(topic)
        if type(found_books) == list:
            for book in found_books:
                self.format_book_data(book)
        else:
            print(found_books)
            
    def search_by_author(self, author):
        found_books = []

        for book in self.book_list:
            if book.author == author:
                found_books.append(book)

        if found_books:
            return found_books
        else:
            return "Autor não encontrado!"

    def show_by_author(self, author):
        found_books = self.search_by_author(author)
        if type(found_books) == list:
            for book in found_books:
                self.format_book_data(book)
        else:
            print(found_books)

    def search_book(self, title):
        found_book = False
        for book in self.book_list:
            if book.title == title:
                found_book = book
        if found_book:
            return found_book
        else:
            return "Livro não encontrado!"
        
    def show_book(self, title):
        book = self.search_book(title)
        if type(book) != str:
            self.format_book_data(book)
        else:
            print(book)

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, title):
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)

    def format_book_data(self, book):
        print(f'''
                Título: {book.title}
                Autor: {book.author}
                Data de Lançamento: {book.release_date}
                Tópico: {book.topic}
            ''')

    