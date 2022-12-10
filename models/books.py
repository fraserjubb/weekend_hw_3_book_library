from models.book import *

book_1 = Book("Mistborn: The Final Empire", "Brandon Sanderson", "High Fantasy", True)
book_2 = Book("Storm Front", "Jim Butcher", "Urban Fantasy", True)
book_3 = Book("Dune", "Frank Herbert", "Science Fiction", False)


books = [book_1, book_2, book_3]

def add_new_book_to_library(book):
    books.append(book)

def remove_book_from_library(index):
    books.pop(index)

