from db.run_sql import run_sql
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

def save(book):

    sql = "INSERT INTO books (title, author_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['id'])
        books.append(book)
    return books

def delete(id):

    sql = "DELETE  FROM books WHERE id= %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE book SET (title, author_d, genre) = (%s, %s, %s, %s) WHERE id %s"
    values = [book.title, book.author.id, book.genre, book.id]
    print(values)
    run_sql(sql, values)
