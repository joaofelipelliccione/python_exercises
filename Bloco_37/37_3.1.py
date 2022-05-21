"""
Os estudantes precisam entregar duas listas para passar de ano.
Cada vez que uma lista é entregue, o nome do aluno fica registrado.
É necessário saber como está o andamento da entrega das listas.
A partir dos logs abaixo, crie quatro funções que respondam às perguntas.

Logs:
  estudantes = ["a", "b", "c", "d", "e", "f", "g"]
  lista1_entregues = ["a", "d", "g", "c"]
  lista2_entregues = ["c", "a", "f"]
"""

students_set = set(["a", "b", "c", "d", "e", "f", "g"])
list_1_set = set(["a", "d", "g", "c"])
list_2_set = set(["c", "a", "f"])


"""
1) Quem ainda não entregou a lista 1?
  - Quais letras pertencem à students_set,
  MAS NÃO pertencem à list_1_set?
"""
print(students_set.difference(list_1_set))

"""
2) Quem já entregou as duas listas?
  - Quais letras pertencem à list_1_set E à list_2_set?
"""
print(list_1_set.intersection(list_2_set))

"""
3) Quem já entregou qualquer uma das listas?
  - Quais letras pertencem à list_1_set OU
  à list_2_set?
"""
print(list_1_set.union(list_2_set))

"""
4) Quem ainda não entregou nenhuma das listas?
  - Quais letras pertencem à students_set MAS NÃO pertencem à
  list_1_set OU list_2_set?
"""
print(students_set.difference(list_1_set, list_2_set))
