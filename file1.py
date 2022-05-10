import random


def scramble_word(word):
    return "".join(random.sample(word, len(word)))


print(scramble_word("palavra"))
