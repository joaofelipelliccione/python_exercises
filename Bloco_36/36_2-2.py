"""
A sequência de Fibonacci é uma sequência numérica em que,
partindo dos 2 primeiros números [0, 1], o próximo número será sempre a
soma dos dois anteriores.

Faça uma função recursiva que retorne o enésimo número da sequência
de Fibonacci.
Sequencia de Fibonacci --> [0, 1, 1, 2, 3, 5, 8, 13, 21...]
"""


def fibo_recursive(n):
    fibo_initial_arr = [0, 1]
    if 0 < n < 3:
        return fibo_initial_arr[n - 1]
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)


print(fibo_recursive(9))
