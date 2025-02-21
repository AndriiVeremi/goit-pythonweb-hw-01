from abc import ABC, abstractmethod


class Book:

    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def show_books(self):
        for book in self.books:
            print(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def run(self):
        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            if command == "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                try:
                    year = int(year)
                    self.library.add_book(Book(title, author, year))
                except ValueError:
                    print("Invalid year format. Please enter a valid integer.")
            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                self.library.remove_book(title)
            elif command == "show":
                self.library.show_books()
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    library = Library()
    manager = LibraryManager(library)
    manager.run()

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, title, author, year):
#         book = {"title": title, "author": author, "year": year}
#         self.books.append(book)

#     def remove_book(self, title):
#         for book in self.books:
#             if book["title"] == title:
#                 self.books.remove(book)
#                 break

#     def show_books(self):
#         for book in self.books:
#             print(
#                 f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}'
#             )


# def main():
#     library = Library()

#     while True:
#         command = input("Enter command (add, remove, show, exit): ").strip().lower()

#         if command == "add":
#             title = input("Enter book title: ").strip()
#             author = input("Enter book author: ").strip()
#             year = input("Enter book year: ").strip()
#             library.add_book(title, author, year)
#         elif command == "remove":
#             title = input("Enter book title to remove: ").strip()
#             library.remove_book(title)
#         elif command == "show":
#             library.show_books()
#         elif command == "exit":
#             break
#         else:
#             print("Invalid command. Please try again.")


# if __name__ == "__main__":
#     main()
