from Catalog import Catalog
from Book import Book

class Interface(Catalog):
    def index(self):
        print('''MENU PRINCIPAL - OPÇÕES
              
              1 - Adicionar livro
              2 - Remover Livro
              3 - Mostrar catálogo completo
              4 - Pesquisar livro por nome
              5 - Pesquisar livro por autor
              6 - Pesquisar livro por tópico
              7 - Sair\n''')
        while True:
            option = input("Digite a opção: ")
            if option == "1":
                self.add_book_interface()
            elif option == "2":
                self.remove_book_interface()
            elif option == "3":
                self.show_catalog_interface()
            elif option == "4":
                self.search_book_interface()
            elif option == "5":
                self.search_by_author_interface()
            elif option == "6":
                self.search_by_topic_interface()
            elif option == "7":
                print("Encerrando a aplicação...")
                break
            else:
                print("Opção inválida")
    
    def add_book_interface(self):
        title = input("Digite o título do livro: ")
        author = input("Digite o nome do autor: ")
        release_date = input("Digite o ano de lançamento: ")
        topic = input("Digite o tópico do livro: ")
        book = Book(title, author, release_date, topic)
        self.add_book(book)
        print("Livro adicionado com sucesso!\n")

    def remove_book_interface(self):
        title = input("Digite o título do livro a ser excluído: ")
        self.remove_book(title)
        print("Livro removido com sucesso!\n")

    def show_catalog_interface(self):
        self.show_catalog()

    def search_by_author_interface(self):
        author = input("Digite o nome do autor: ")
        self.show_by_author(author)

    def search_by_topic_interface(self):
        topic = input("Digite o tópico: ")
        self.show_by_topic(topic)

    def search_book_interface(self):
        title = input("Digite o título do livro a ser pesquisado: ")
        self.show_book(title) 

interface = Interface()
interface.index()