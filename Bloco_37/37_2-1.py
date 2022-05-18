"""
Crie um dicionário que mapeia inteiros de 3 a 20 para o seu dobro.
  Exemplo: {3: 6, 4: 8, 5: 10}
"""

arr = list(range(3, 21))  # [1, 2, 3,..., 20]
dc = {key: key * 2 for key in arr}

print(dc)
