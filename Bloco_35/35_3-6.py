"""
Escreva um programa que se conecte ao banco de dados 'library'
e liste os livros da coleção 'books', para uma determinada categoria informada
pelo usuário.
Somente o título dos livros deve ser exibido.
"""
import json
from pymongo import MongoClient


def populate_db():
    with open("./Assets/books.json") as file:
        books_arr = json.load(file)
        with MongoClient("mongodb://localhost:27017/") as client:
            db = client.library
            db.books.insert_many(books_arr)


"""Chame essa função, caso deseje criar e popular
a coleção books, do banco library."""
# populate_db()


def get_book_titles_from_category(category):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client.library
        for book in db.books.find({"categories": category}):
            print(book["title"])


print(get_book_titles_from_category("Internet"))
