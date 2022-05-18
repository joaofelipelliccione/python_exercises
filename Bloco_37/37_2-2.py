"""
Dada uma string, construa um dicionário com a contagem
de cada caractere da palavra.
    Ex:
    str = "bbbbaaaaaacccd"
    saída: {b: 4, a: 6, c: 3, d: 1}
"""


def count_characters(string):
    result = {}

    for letter in string:
        if not result.get(letter):
            result[letter] = 1
        else:
            result[letter] += 1

    return result


print(count_characters("João"))
print(count_characters("Felipe"))
