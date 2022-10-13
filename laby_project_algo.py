import random
import turtle
from copy import deepcopy


# paramètres de base turtle
# orientation intiale de la tête (vers la droite de l’écran)
turtle.setheading(0)
# on cache la tortue
turtle.hideturtle()
# on accélère la tortue
turtle.speed(0)
# couleur et taille du trait
turtle.color("black", "black")
turtle.pensize(3)


class Pile:
    """
    Classe Pile
    création d'une instance Pile avec une liste
    """

    def __init__(self):
        """
        Initialisation d'une pile vide
        """
        self.L = []

    def vide(self):
        """
        Teste si la pile est vide, renvoie un boolean
        """
        return self.L == []

    def depiler(self):
        """
        Dépile
        """
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def empiler(self, x):
        """
        Empile
        """
        self.L.append(x)

    def taille(self):
        """
        Renvoie la taille de la pile
        """
        return len(self.L)

    def sommet(self):
        """
        Renvoie le sommet de la pile
        """
        assert not self.vide(), "Pile vide"
        return self.L[-1]


class Laby:
    """
    Classe Laby
    création puis résolution du labyrinthe
    """

    # variable du labyrinthe
    laby = []
    # variable des murs (-> [Haut, Bas, Gauche, Droite])
    walls = []
    # nombre de colonnes
    m = 0
    # nombre de lignes
    n = 0

    def __init__(self, m, n):
        """
        Initialisation du layrinthe
        Appelle directement la fonction de création de la base, puis de modélisation du labyrinthe
        """
        self.m = m
        self.n = n
        # base pour le labyrinthe
        self.make_base()
        # fusions aléatoires des chemins
        self.make_fusions()

    def make_base(self):
        """
        Génération de la bases du labyrinthe
        """
        # chiffres pour les cases (de 0 à n*m)
        laby_numbers = list(range(self.m*self.n))
        # base du labyrinthe (avec chiffres)
        self.laby = [[laby_numbers.pop(0) for colonne in range(self.m)]
                     for ligne in range(self.n)]
        # base pour les murs (chaque case entourée de tous les murs)
        self.walls = [[[1, 1, 1, 1]
                       for colonne in range(self.m)] for ligne in range(self.n)]

    def make_fusions(self):
        """
        Ruptures des murs et fusions des chemins jusqu'à ce que le nombre de fusions atteigne m*n-1
        """
        # variable pour compter le nombre de fusions
        fusions_count = 0
        while fusions_count < self.m*self.n-1:
            # choix aléatoire des index d'une case
            random_line_index1 = random.randrange(0, self.n)
            random_column_index1 = random.randrange(0, self.m)
            # variable du mur 1
            random_chosen_wall1 = self.walls[random_line_index1][random_column_index1]
            # liste des choix pour les directions
            direction_choices_index = list(range(4))
            # suppression des choix impossibles (si ce choix peut sortir du labyrinthe)
            if random_line_index1 == 0:
                direction_choices_index.remove(0)
            if random_line_index1 == (self.n-1):
                direction_choices_index.remove(1)
            if random_column_index1 == 0:
                direction_choices_index.remove(2)
            if random_column_index1 == (self.m-1):
                direction_choices_index.remove(3)
            # suppression des murs déjà rompus
            for wall_index in random_chosen_wall1:
                if random_chosen_wall1[wall_index] == 0 and wall_index in direction_choices_index:
                    direction_choices_index.remove(wall_index)
            # choix aléatoire de la direction du mur ([H, B, G, D])
            if len(direction_choices_index) == 0:
                continue
            random_wall_index1 = random.choice(direction_choices_index)
            # variable de la première case
            case1 = self.laby[random_line_index1][random_column_index1]
            # index de la seconde case et du second mur selon la direction du mur à fusionner
            if random_wall_index1 == 0:
                random_line_index2 = random_line_index1 - 1
                random_column_index2 = random_column_index1
                random_wall_index2 = 1
            elif random_wall_index1 == 1:
                random_line_index2 = random_line_index1 + 1
                random_column_index2 = random_column_index1
                random_wall_index2 = 0
            elif random_wall_index1 == 2:
                random_line_index2 = random_line_index1
                random_column_index2 = random_column_index1 - 1
                random_wall_index2 = 3
            elif random_wall_index1 == 3:
                random_line_index2 = random_line_index1
                random_column_index2 = random_column_index1 + 1
                random_wall_index2 = 2
            # variable de la seconde case
            case2 = self.laby[random_line_index2][random_column_index2]
            # détermination du chiffre le plus bas
            lower_number = case1 if case1 < case2 else case2
            # vérification si les cases ne sont pas déjà fusionnées
            if case1 != case2:
                # rupture du mur
                self.walls[random_line_index1][random_column_index1][random_wall_index1] = 0
                self.walls[random_line_index2][random_column_index2][random_wall_index2] = 0
                # fusion des cases
                for ligne_index in range(len(self.laby)):
                    self.laby[ligne_index] = [
                        number if number != case1 and number != case2 else lower_number for number in self.laby[ligne_index]]
                # incrémentation du nombre de fusions
                fusions_count = fusions_count + 1

    def resolve(self, entree=None, sortie=None):
        """
        Renvoie une pile qui permet de résoudre le labyrinthe
        """
        # vérification des variables d'entrée et sortie
        assert entree == None or (
            0 <= entree[0] <= self.n-1 and 0 <= entree[1] <= self.m-1), "Les coordonnées d'entrée sont incorrectes"
        assert sortie == None or (
            0 <= sortie[0] <= self.n-1 and 0 <= sortie[1] <= self.m-1), "Les coordonnées de sortie sont incorrectes"
        # création variables d'entrée et sortie
        if not entree:
            entree = (0, 0)
        if not sortie:
            sortie = (self.n-1, self.m-1)
        # copie du laby
        T = deepcopy(self.laby)
        # début de l'algorithme
        p = Pile()
        v = entree
        T[v[0]][v[1]] = -1
        recherche = True
        while recherche:
            vois = self.neighbors(T, v)
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

    def neighbors(self, T, v):
        """
        Renvoie les voisins autour d'une case
        """
        V = []
        i, j = v[0], v[1]
        walls = self.walls[i][j]
        # recherche les cases sans mur autour, ainsi que l'état de visite de la case (différent de -1)
        for wall_index in range(len(walls)):
            if walls[wall_index] == 0:
                if wall_index == 0 and T[i-1][j] != -1:
                    V.append((i-1, j))
                elif wall_index == 1 and T[i+1][j] != -1:
                    V.append((i+1, j))
                elif wall_index == 2 and T[i][j-1] != -1:
                    V.append((i, j-1))
                elif wall_index == 3 and T[i][j+1] != -1:
                    V.append((i, j+1))
        return V

    def tracage_laby(self, resolution_pile, taille_case=50):
        """
        Dessine le labyrinthe et sa résolution
        """
        # Coordonnés du coin haut gauche du labyrinthe dans la fenêtre turtle
        coord = (-500, 400)
        turtle.penup()
        turtle.goto(coord[0], coord[1])
        turtle.pendown()

        for i in range(len(self.walls)):
            # Double boucle "for" pour chaque case en longueur et chaque case en largueur
            for j in range(len(self.walls[0])):
                # On vérifie si il y a un mur supérieur
                if i == 0 or self.walls[i][j][0] == 0:
                    turtle.penup()
                turtle.forward(taille_case)
                turtle.pendown()
                # On vérifie si il y a un mur à droite.
                if self.walls[i][j][3] == 1:
                    turtle.right(90)
                    turtle.forward(taille_case)
                    turtle.backward(taille_case)
                    turtle.left(90)
                # On ne vérifie pas les autres murs pour économiser du temps de traçage et calcul
            # On passe à la ligne d'après
            turtle.penup()
            turtle.backward(taille_case*len(self.walls[0]))
            turtle.right(90)
            turtle.forward(taille_case)
            turtle.left(90)
            turtle.pendown()

        # On trace les contours du labyrinthe
        turtle.goto(coord[0], coord[1])
        for i in range(2):
            turtle.pensize(5)
            turtle.forward(len(self.walls[0])*taille_case)
            turtle.right(90)
            turtle.forward(len(self.walls)*taille_case)
            turtle.right(90)
            turtle.pensize(3)

        # Traçage de la flèche de fin
        if resolution_pile != False:
            arrivee = resolution_pile.depiler()
            turtle.penup()
            turtle.goto((arrivee[1]+1)*taille_case-taille_case/2 +
                        coord[0], -arrivee[0]*taille_case-taille_case/2+coord[1])
            turtle.pendown()
            turtle.color("green")
            turtle.left(45)
            turtle.forward(taille_case/2)
            turtle.backward(taille_case/2)
            turtle.left(90)
            turtle.forward(taille_case/2)
            turtle.backward(taille_case/2)
            turtle.right(135)

        # On trace la résolution du labyrinthe
        if resolution_pile != False:
            for i in range(resolution_pile.taille()):
                aller = resolution_pile.depiler()
                turtle.goto((aller[1]+1)*taille_case-taille_case/2 +
                            coord[0], -aller[0]*taille_case-taille_case/2+coord[1])

        turtle.showturtle()

        turtle.exitonclick()


Labyri = Laby(10, 10)
# test des erreurs pour les coordonnées
# Labyri.tracage_laby(Labyri.resolve((0, 10), (9, 0)))
# Labyri.tracage_laby(Labyri.resolve((0, 8), (18, 0)))
Labyri.tracage_laby(Labyri.resolve((0, 0), (0, 0)))
