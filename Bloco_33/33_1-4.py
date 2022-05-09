"""Crie uma função que receba um array de nomes e retorne o nome com a maior
quantidade de caracteres."""


def name_with_higher_length(arr_of_names):
    last_name = ""
    for name in arr_of_names:
        if len(name) > len(last_name):
            last_name = name

    return last_name


arr_to_test = ["Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
print(name_with_higher_length(arr_to_test))
#  "Fernanda"
