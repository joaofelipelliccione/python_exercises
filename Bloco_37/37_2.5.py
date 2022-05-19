"""
Quais elementos da lista A, também ocorrem na lista B?
Ou seja, qual a interseção entre as listas?

Ex:
  lista_A = [1, 2, 3, 4, 5, 6]
  lista_B = [4, 5, 6, 7, 8, 9]
  resposta = [4, 5, 6]
"""


def intersection(arr_A, arr_B):
    result = []

    for num_A in arr_A:
        if num_A in arr_B:
            result.append(num_A)

    return result


print(intersection([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]))
