#  Exercício do Blefe:


def blefe(obj):
    player_A_set = set(list(obj.items())[0][1])
    player_B_set = set(list(obj.items())[1][1])
    player_A_finals = player_A_set.difference(player_B_set)
    player_B_finals = player_B_set.difference(player_A_set)

    player_A_score = max(player_A_finals) - min(player_A_finals)
    player_B_score = max(player_B_finals) - min(player_B_finals)

    if player_A_score > player_B_score:
        return list(obj.items())[0][0]
    else:
        return list(obj.items())[1][0]


game = {"Clara": [0, 1, 5, 9, 10], "Marco": [0, 2, 8, 9, 10]}
print(blefe(game))
