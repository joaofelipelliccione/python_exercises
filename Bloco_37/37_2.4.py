"""
Separe as palavras de um array, de acordo com suas
respectivas letras iniciais.

Ex: test_arr = [Luíza, João, Luana, Pedro, José, Luciana, Maria]
{
  J: [João, José],
  L: [Luíza, Luana, Luciana],
  M: [Maria],
  P: [Pedro],
}
"""


def separate(names_arr):
    storage = {}

    for name in names_arr:
        if not storage.get(name[0]):
            storage[name[0]] = [name]
        else:
            storage[name[0]].append(name)

    return dict(sorted(storage.items()))


test_arr = [
    "Luíza",
    "João",
    "Madalena",
    "Josimar",
    "Pedro",
    "José",
    "Maria",
    "Joaquim",
]
print(separate(test_arr))
