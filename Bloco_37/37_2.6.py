"""Bloco 37.2 (Hashmap e Dict) - Exercício 1 Facebook"""


def fb_exercise(words_arr, chars):
    obj = {key: 0 for key in words_arr}
    result = []

    for key in obj:
        for letter in chars:
            if letter in key:
                obj[key] += 1
    # print(obj)

    for key in obj:
        if len(key) <= obj[key]:
            result.append(key)

    return result


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(fb_exercise(words, chars))

words2 = ["hello", "world", "students"]
chars2 = "welldonehoneyr"
print(fb_exercise(words2, chars2))
