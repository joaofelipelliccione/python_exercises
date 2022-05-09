"""Exercício: Crie uma função que receba quantos números
quiser e retorne a média aritmética deles."""


def average(*nums):
    sum = 0

    for num in nums:
        sum += num

    return sum / len(nums)


print(average(5, 10, 15, 20))
#  12.5
