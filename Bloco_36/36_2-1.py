"""
Faça um algoritmo recursivo de soma. Esse, deve receber um N° como argumento
para, então, somar todos os números antecessores a ele.
"""


def recursive_sum(num):
    if num == 0:
        return 0
    else:
        return num + recursive_sum(num - 1)


print(recursive_sum(4))
