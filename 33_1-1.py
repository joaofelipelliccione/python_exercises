"""Exercício: Crie uma função que receba quantos números
quiser e retorne o maior deles."""


def higher_num(*nums):
    arr = [num for num in nums]
    arr.sort()
    return arr[-1]


print(higher_num(10, 5, 80, 1))
#  80