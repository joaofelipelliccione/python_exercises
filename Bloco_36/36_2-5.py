"""
Crie um algoritmo recursivo para contar quantos números pares
existem em uma sequência numérica (1 a n).
"""


def how_many_evens(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            return 1 + how_many_evens(n - 1)
        else:
            return 0 + how_many_evens(n - 1)


print(how_many_evens(10))
