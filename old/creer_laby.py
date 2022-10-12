import random
from copy import deepcopy

from cours import Pile


def voisins(T, v):
    lignes = len(T)
    colonnes = len(T[0])
    V = []
    i, j = v[0], v[1]
    for a in (-1, 1):
        if 0 <= i+a < lignes:
            if T[i+a][j] > 0:
                V.append((i+a, j))
        if 0 <= j+a < colonnes:
            if T[i][j+a] > 0:
                V.append((i, j+a))
    return V


def entire_path_indexes(laby, indexes_tuple):
    all_indexes = [indexes_tuple]
    path_queue = [indexes_tuple]
    while len(path_queue) > 0:
        current_neighbors = [neighbor for neighbor in voisins(
            laby, path_queue.pop(0)) if neighbor not in all_indexes]
        all_indexes += current_neighbors
        path_queue += current_neighbors
    return all_indexes


# laby_base = [[1, 0, 2, 0, 2],
#              [0, 0, 2, 0, 2],
#              [2, 2, 2, 2, 2],
#              [0, 0, 0, 0, 0],
#              [7, 0, 8, 0, 9]
#              ]
# once this work, change the for loop below make sure it makes enough iterations
# needs to work then
# print(entire_path_indexes(laby_base, (2, 2)))
# exit()


def creer_laby(m, n):
    # -------------------------------------
    # base pour le labyrinthe
    # -------------------------------------
    laby_base = []
    laby_numbers = list(range(1, m*n+1))
    for ligne in range(n):
        ligne1 = []
        for colonne in range(m):
            ligne1.append(laby_numbers.pop(0))
            if colonne != m-1:
                ligne1.append(0)
        ligne2 = [0 for colonne in range(2*m-1)]
        laby_base.append(ligne1)
        if ligne != n-1:
            laby_base.append(ligne2)
    # -------------------------------------
    # début de la fusion aléatoire de chemin
    # -------------------------------------
    # création des listes d'index
    lignes_index_impaires = list(range(1, 2*n-1, 2))
    colonnes_index_paires = list(range(0, 2*m-1, 2))
    lignes_index_paires = list(range(0, 2*n-1, 2))
    colonnes_index_impaires = list(range(1, 2*m-1, 2))
    # liste pour choix aléatoires
    lignes_impaires_colonnes_paires = [(ligne_index, colonne_index)
                                       for ligne_index in lignes_index_impaires for colonne_index in colonnes_index_paires]
    lignes_paires_colonnes_impaires = [(ligne_index, colonne_index)
                                       for ligne_index in lignes_index_paires for colonne_index in colonnes_index_impaires]
    index_choices = lignes_impaires_colonnes_paires + lignes_paires_colonnes_impaires
    random.shuffle(index_choices)
    # début des fusions
    # for fusion_index in range(1):
    opened_walls_number = 0
    while opened_walls_number < m*n+1:
        # randomly choose an index tuple
        random_index_tuple = index_choices.pop(0)
        # find tuple indexes of elements to replace
        if random_index_tuple[0] % 2 != 0:
            neighbors_to_merge_1 = entire_path_indexes(
                laby_base, (random_index_tuple[0]-1, random_index_tuple[1]))
            neighbors_to_merge_2 = entire_path_indexes(
                laby_base, (random_index_tuple[0]+1, random_index_tuple[1]))
            if laby_base[random_index_tuple[0]-1][random_index_tuple[1]] == laby_base[random_index_tuple[0]+1][random_index_tuple[1]]:
                continue
            lower_number = laby_base[random_index_tuple[0]-1][random_index_tuple[1]] if laby_base[random_index_tuple[0]-1][random_index_tuple[1]
                                                                                                                           ] < laby_base[random_index_tuple[0]+1][random_index_tuple[1]] else laby_base[random_index_tuple[0]+1][random_index_tuple[1]]
        else:
            neighbors_to_merge_1 = entire_path_indexes(
                laby_base, (random_index_tuple[0], random_index_tuple[1]-1))
            neighbors_to_merge_2 = entire_path_indexes(
                laby_base, (random_index_tuple[0], random_index_tuple[1]+1))
            if laby_base[random_index_tuple[0]][random_index_tuple[1] - 1] < laby_base[random_index_tuple[0]][random_index_tuple[1]+1]:
                continue
            lower_number = laby_base[random_index_tuple[0]][random_index_tuple[1]-1] if laby_base[random_index_tuple[0]][random_index_tuple[1] -
                                                                                                                         1] < laby_base[random_index_tuple[0]][random_index_tuple[1]+1] else laby_base[random_index_tuple[0]][random_index_tuple[1]+1]
        tuple_indexes_to_merge = neighbors_to_merge_1 + \
            neighbors_to_merge_2 + [random_index_tuple]
        # merge by replacing all elements
        for tuple_index in tuple_indexes_to_merge:
            laby_base[tuple_index[0]][tuple_index[1]] = lower_number
        # increment opened walls
        opened_walls_number += 1
    return laby_base


for l in creer_laby(3, 4):
    print(l)

for _ in range(10000):
    laby = creer_laby(3, 5)
    for l in laby:
        for c in l:
            if c > 1:
                print("PROBLEME")
                exit()
