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
        with MongoClient() as client:
            db = client.library
            db.books.insert_many(books_arr)


populate_db()
