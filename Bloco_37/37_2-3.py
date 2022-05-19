"""
Encontre o N° mais frequente em um array.
Caso haja empate, retorne qualquer um dos empatados.
"""


def most_frequent_number(arr):
    storage = {}

    for num in arr:
        if not storage.get(num):
            storage[num] = 1
        else:
            storage[num] += 1

    sorted_storage = dict(
        sorted(storage.items(), key=lambda item: item[1], reverse=True)
    )
    return list(sorted_storage.items())[0][0]


test_arr = [3, 5, 1, 8, 3, 5, 5, 3, 5]
print(most_frequent_number(test_arr))
