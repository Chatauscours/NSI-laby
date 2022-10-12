class Pile:
    """classe Pile
    création d'une instance Pile avec une liste
    """

    def __init__(self) -> None:
        "Initialisation d'une pile vide"
        self.L = []

    def vide(self):
        "teste si la pile est vide"
        return self.L == []

    def depiler(self):
        "dépile"
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def empiler(self, x):
        "empile"
        self.L.append(x)

    def taille(self):
        """Renvoie la taille de la pile"""
        return len(self.L)

    def sommet(self):
        """Renvoie le sommet de la pile"""
        assert not self.vide(), "Pile vide"
        return self.L[-1]


# p = Pile()
# for i in range(5):
#     p.empiler(2*i)
# print(p.L)
# a = p.depiler()
# print(a)
# print(p.L)
# print(p.vide())
# print(p.taille())
# print(p.sommet())


# def pile():
#     # retourne une liste vide
#     return []


# # vide
# def vide(p):
#     """renvoie True si la pile est vide
#     et False sinon"""
#     return p == []


# # empiler
# def empiler(p, x):
#     "Ajoute l'élément x à la pile p"
#     p.append(x)


# # dépiler
# def depiler(p):
#     "dépile et renvoie l'élément au sommet de la pile p"
#     assert not vide(p), "Pile vide"
#     return p.pop()


# # taille
# def taille(p):
#     """Renvoie la taille de la pile"""
#     return len(p)


# # sommet
# def sommet(p):
#     """Renvoie le sommet de la pile"""
#     return p[-1]


# p = pile()
# for i in range(5):
#     empiler(p, 2*i)
# a = depiler(p)
# print(a)
# print(vide(p))
# print(taille(p))
# print(sommet(p))
