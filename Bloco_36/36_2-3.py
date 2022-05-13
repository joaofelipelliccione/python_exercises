"""Faça uma função recursiva que recebe um array
e o retorna na ordem reversa."""


def reverse_arr(arr):
    if len(arr) < 2:
        return arr
    else:
        print(arr[1:])
        print([arr[0]])
        return reverse_arr(arr[1:]) + [arr[0]]


test_arr = ["A", "B", "C", "D"]
print(reverse_arr(test_arr))
