"""
Utilize o módulo random para gerar um array com 100 números.
Cada um desses números deve ser a média de 10 números gerados aleatóriamente.

Qual é a ordem de complexidade de tempo e de espaço deste programa?
0(n) e 0(1), respectivamente.
"""

import random


def get_int_from_average_of_ten():
    counter = 1
    arr_of_ten = []
    sum_of_ten = 0

    while counter <= 10:
        arr_of_ten.append(random.randint(1, 100))
        counter += 1

    for num in arr_of_ten:
        sum_of_ten += num

    return sum_of_ten / 10


def get_hundred_arr():
    counter = 1
    hundred_arr = []

    while counter <= 100:
        hundred_arr.append(get_int_from_average_of_ten())
        counter += 1

    return hundred_arr


print(get_hundred_arr())
