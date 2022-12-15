from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book 
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    print(books)
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route("/books/<id>/edit", methods = ['GET'])
def update_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_athors = authors)