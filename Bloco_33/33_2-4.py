"""Dado o arquivo books.json, leia seu conteúdo e calcule a porcentagem de
livros em cada categoria, sempre com relação ao número total de livros.
O resultado deve ser escrito em um arquivo no formato CSV."""
import json
import csv


def retrieve_books():
    with open("./Assets/books.json") as file:
        return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 1
            else:
                categories[category] += 1

    return categories


def build_csv_report():
    books_arr = retrieve_books()
    num_of_books = len(books_arr)
    categories_dict = count_books_by_categories(books_arr)
    headers = ["categoria", "porcentagem"]

    with open("./Assets/report.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for category in categories_dict:
            percentage = categories_dict[category] / num_of_books
            writer.writerow([category, percentage])


books = retrieve_books()
cat_dict = count_books_by_categories(books)
print(cat_dict)

build_csv_report()
