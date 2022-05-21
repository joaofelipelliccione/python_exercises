"""
Dada uma lista que representa várias jogadas de um dado de 6 faces,
combine as jogadas que somam 7. Cada jogada só pode ser utilizada em
uma soma.

rolls: [1, 5, 3, 2, 6, 1, 4, 2, 6, 3, 1, 1]
"""


def soma_7(rolls):
    seen_before = set()
    result = []

    for roll in rolls:
        if 7 - roll in seen_before:  # Caso o complemento de roll (7-1) exista no set.
            result.append((roll, 7 - roll))
            seen_before.discard(7 - roll)
        else:
            seen_before.add(roll)

    return result


rolls = [1, 5, 3, 2, 6, 1, 4, 2, 6, 3, 1, 1]
print(soma_7(rolls))
