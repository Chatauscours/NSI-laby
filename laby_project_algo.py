import random


class Laby:
    # variable du labyrinthe
    laby = []
    # variable des murs (-> [H, B, G, D])
    walls = []
    # nombre de colonnes
    m = 0
    # nombre de lignes
    n = 0

    def __init__(self, m, n):
        self.m = m
        self.n = n
        # base pour le labyrinthe
        self.make_base()
        # début de la fusion aléatoire de chemins
        self.make_fusions()

    def make_base(self):
        """
        Génération de la bases du labyrinthe
        """
        laby_numbers = list(range(self.m*self.n))
        self.laby = [[laby_numbers.pop(0) for colonne in range(self.m)]
                     for ligne in range(self.n)]
        self.walls = [[[1, 1, 1, 1]
                       for colonne in range(self.m)] for ligne in range(self.n)]

    def make_fusions(self):
        """
        Ruptures des murs et fusions des chemins jusqu'à ce que le nombre de fusions atteigne m*n-1
        """
        fusions_count = 0
        while fusions_count < self.m*self.n-1:
            # choix aléatoire des indexes d'une case
            random_line_index1 = random.randrange(0, self.n)
            random_column_index1 = random.randrange(0, self.m)
            # variable du mur 1
            random_chosen_wall1 = self.walls[random_line_index1][random_column_index1]
            # liste des choix pour les directions
            direction_choices_index = list(range(4))
            # suppression des choix impossibles
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
            # indexes de la seconde case et du second mur selon la direction du mur à fusionner
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

    @property
    def laby_walls_around(self):
        """
        Retourne la version du labyrinthe avec les murs autour
        PAS TERMINÉ !!
        """
        laby_walls_around = []
        for line_index in range(self.n):
            upper_line = []
            current_line = []
            lower_line = []
            for column_index in range(self.m):
                # mur haut
                upper_line.append(1)
                upper_line.append(self.walls[line_index][column_index][0])
                upper_line.append(1)
                # mur bas
                lower_line.append(1)
                lower_line.append(self.walls[line_index][column_index][1])
                lower_line.append(1)
                # mur gauche
                current_line.append(self.walls[line_index][column_index][2])
                # case
                current_line.append(self.laby[line_index][column_index])
                # mur droit
                current_line.append(self.walls[line_index][column_index][3])
            laby_walls_around.append(upper_line)
            laby_walls_around.append(current_line)
            laby_walls_around.append(lower_line)
        return laby_walls_around

    def voisins(self, v):
        lignes = len(self.laby)
        colonnes = len(self.laby[0])
        V = []
        i, j = v[0], v[1]
        for a in (-1, 1):
            if 0 <= i+a < lignes:
                if self.laby[i+a][j] > 0:
                    V.append((i+a, j))
            if 0 <= j+a < colonnes:
                if self.laby[i][j+a] > 0:
                    V.append((i, j+a))
        return V


labyrinthe = Laby(4, 5)
for l in labyrinthe.laby:
    print(l)
for w in labyrinthe.walls:
    print(w)
# print("-"*40)
# for l in labyrinthe.laby_walls_around:
#     print(l)
