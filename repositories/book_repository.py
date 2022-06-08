from db.run_sql import run_sql

from models.author import Author 
from models.book import Book 

def save(book):
    sql = "INSERT INTO books (title, edition, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.edition, book.author_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id

    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for result in results: 
        book = Book(result["title"], result["edition"], result["author_id"], result["id"])
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id=%s"
    values = [id]
    run_sql(sql, values) 

