"""Dado o arquivo books.json, leia seu conteúdo e calcule a porcentagem de
livros em cada categoria, sempre com relação ao número total de livros.
O resultado deve ser escrito em um arquivo no formato CSV."""
import json

categories_from_books = []


def retrieve_books():
    with open("./Assets/books.json") as file:
        return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            else:
                categories[category] += 1

    return categories


books_arr = retrieve_books()
categories_dict = count_books_by_categories(books_arr)
print(categories_dict)
