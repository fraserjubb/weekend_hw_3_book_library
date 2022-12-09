from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book_to_library, remove_book_from_library
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_new_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title=title, author=author, genre=genre)
    add_new_book_to_library(new_book)
    return redirect('/books')

@app.route('/books/<book>')
def book(book):
    return render_template('book.html', title="book", book=books[int(book)])
    # return redirect('/books/<book>')


@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    remove_book_from_library(int(index))
    return redirect('/books')




