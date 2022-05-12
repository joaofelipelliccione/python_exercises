"""
Crie um algoritmo recursivo para contar quantos números pares
existem em uma sequência numérica (1 a n).
"""


def how_many_evens(n):
    sequence = list(range(1, n + 1))
    if n == len(sequence):
        return 0
    else:
        sequence[-1]


print(how_many_evens(5))
