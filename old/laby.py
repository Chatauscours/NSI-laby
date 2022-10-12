from copy import deepcopy
from cours import Pile

laby = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

# laby_base = [[0, -, 1, -, 2],
#              [-, -, -, -, -],
#              [3, -, 4, -, 5]]
# lignes impaires, colonnes paires
# lignes paires, colonnes impaires

lignes = len(laby)
colonnes = len(laby[0])

# for ligne in laby:
#     print(ligne)


# renvoie une liste de tuple d'indexes (ligne, colonne) pour savoir quel chemin est disponible autour du tuple d'indexes donné en argument v
def voisins(T, v):
    V = []
    i, j = v[0], v[1]
    for a in (-1, 1):
        if 0 <= i+a < lignes:
            if T[i+a][j] == 1:
                V.append((i+a, j))
        if 0 <= j+a < colonnes:
            if T[i][j+a] == 1:
                V.append((i, j+a))
    return V


# renvoie [(1, 1)] car le seul chemin disponible depuis le départ (0, 1) est en (1, 1)
# print(voisins(laby, (0, 1)))


def parcours(laby, entree, sortie):
    T = deepcopy(laby)
    p = Pile()
    v = entree
    T[v[0]][v[1]] = -1
    recherche = True
    while recherche:
        vois = voisins(T, v)
        if len(vois) == 0:
            if p.vide():
                return False
            else:
                v = p.depiler()
        else:
            p.empiler(v)
            v = vois[0]
            T[v[0]][v[1]] = -1
            if v == sortie:
                p.empiler(v)
                recherche = False
    return p


# laby_pile = parcours(laby, (0, 1), (5, 4))
# for l in laby:
#     print(l)
# print("-"*40)

# laby_avec_parcours = deepcopy(laby)
# while not laby_pile.vide():
#     index_tuple = laby_pile.depiler()
#     laby_avec_parcours[index_tuple[0]][index_tuple[1]] = 2
# for l in laby_avec_parcours:
#     print(l)
