"""
Escreva um programa que retorne uma lista com os valores numéricos de 1 a N,
com as seguintes exceções:
    - Números divisíveis por 3 deve aparecer como 'Fizz',
    ao invés do número;
    - Números divisíveis por 5 devem aparecer como 'Buzz,
    ao invés do número;
    - Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz',
    ao invés do número';
Ex: 3 -> [1, 2, "Fizz"].
"""


def fb(number):
    result_arr = []
    numbers_arr = list(range(1, number + 1))

    for num in numbers_arr:
        if num % 3 == 0 and num % 5 == 0:
            result_arr.append("FizzBuzz")
        elif num % 3 == 0:
            result_arr.append("Fizz")
        elif num % 5 == 0:
            result_arr.append("Buzz")
        else:
            result_arr.append(num)

    return result_arr


print(fb(15))
