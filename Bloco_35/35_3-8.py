"""
  Vá ao site https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags e
  recupere as imagens de todas as bandeiras.
"""

import requests
from parsel import Selector

END_POINT = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"


def get_selector(url):
    try:
        response = requests.get(url, timeout=5)
    except Exception:
        return "Algo deu errado."
    else:
        selector = Selector(text=response.text)
        return selector


def get_all_flags(url):
    flags_dict = {}
    counter = 0
    page_selector = get_selector(url)

    if page_selector == "Algo deu errado.":
        return "Request não realizada :("
    else:
        for a in page_selector.css("a.image"):
            src = a.css("img::attr(src)").get()
            flags_dict[f"flag_{counter}"] = f"https:{src}"
            counter += 1

    return flags_dict


print(get_all_flags(END_POINT))
