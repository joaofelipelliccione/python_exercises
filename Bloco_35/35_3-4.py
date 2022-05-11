"""
Baseado em uma página contendo detalhes sobre um livro, faça a extração dos
campos:
  - título;
  - preço (somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76.);
  - descrição (sem sufixo "more...") e
  - url contendo a imagem de capa do livro.
Os campos extraídos devem ser apresentados separados por vírgula.
  - Ex: título, preço, descrição, capa.
"""
import requests
from parsel import Selector

END_POINT = (
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
)


def get_selector(url):
    try:
        response = requests.get(url, timeout=5)
    except Exception:
        return "Algo deu errado."
    else:
        selector = Selector(text=response.text)
        return selector


def get_required_gaps(url):
    book_selector = get_selector(END_POINT)

    if book_selector == "Algo deu errado.":
        return "Request não realizada :("
    else:
        title = book_selector.css("div.product_main > h1::text").get()
        price = book_selector.css("p.price_color::text").re_first(
            r"£\d+\.\d{2}"
        )
        description = book_selector.css("#product_description ~ p::text").get()
        clean_description = description[:-len("...more")]
        img_url = book_selector.css("div.item > img::attr(src)").get()
        return f"""
        Título: {title}
        Preço: {price}
        Descrição: {clean_description}:
        URL da Capa: {img_url}"""


print(get_required_gaps(END_POINT))
