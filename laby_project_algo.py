import random
import turtle
from copy import deepcopy
# orientation intiale de la tête :
#vers la droite de l’écran
turtle.setheading(0)
turtle.hideturtle() # on cache la tortue
turtle.speed(0) # on accélère la tortue
turtle.color("black", "black")
turtle.pensize(3)

class Pile:
    def __init__(self):
        self.L=[]
    
    def vide(self):
        return self.L==[]
    
    def depiler(self):
        assert not self.vide(),"Pile vide"
        return self.L.pop()
    
    def empiler(self,x):
        "empile"
        self.L.append(x)
    
    def taille(self):
        l=len(self.L)
        return l
    
    def sommet(self):
        l=len(self.L)
        s=(self.L[l-1])
        return s

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

    def resolve(self, entree=None, sortie=None):
        """
        Renvoie une pile qui permet de résoudre le labyrinthe
        """
        # variables d'entrée et sortie
        if not entree:
            entree = (0, 0)
        if not sortie:
            sortie = (self.n-1, self.m-1)
        T = deepcopy(self.laby)
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
    
    def tracage_laby(self,murs,chemin,taille_case=75):
        coord=(-500,400) #Coorddonnés du coin haut gauche du labyrinthe dans la fenêtre turtle
        turtle.penup()
        turtle.goto(coord[0],coord[1])
        turtle.pendown()
        
        for i in range(len(murs)): 
            for j in range(len(murs[0])): #Double boucle "for" pour chaque case en longueur et chaque case en largueur
                if i == 0 or murs[i][j][0] == 0: #On vérifie si il y a un mur supérieur
                    turtle.penup()
                turtle.forward(taille_case)
                turtle.pendown()
                if murs[i][j][3] == 1: #On vérifie si il y a un mur à droite.
                    turtle.right(90)
                    turtle.forward(taille_case)
                    turtle.backward(taille_case)
                    turtle.left(90)
            turtle.penup()
            turtle.backward(taille_case*len(murs[0]))
            turtle.right(90)
            turtle.forward(taille_case)
            turtle.left(90)
            turtle.pendown()
        
        turtle.goto(coord[0],coord[1])
        for i in range(2):
            turtle.pensize(5)
            turtle.forward(len(murs[0])*taille_case)
            turtle.right(90)
            turtle.forward(len(murs)*taille_case)
            turtle.right(90)
            turtle.pensize(3)
        
        chemin=self.resolve()
        arrivee=chemin.depiler()
        
        turtle.penup()
        turtle.goto((arrivee[1]+1)*taille_case-taille_case/2+coord[0],-arrivee[0]*taille_case-taille_case/2+coord[1])
        turtle.pendown()
        turtle.color("green")
        turtle.left(45)
        turtle.forward(taille_case/2)
        turtle.backward(taille_case/2)
        turtle.left(90)
        turtle.forward(taille_case/2)
        turtle.backward(taille_case/2)
        turtle.right(135)
        
        for i in range(chemin.taille()):
            aller=chemin.depiler()
            turtle.goto((aller[1]+1)*taille_case-taille_case/2+coord[0],-aller[0]*taille_case-taille_case/2+coord[1])
            
        continuer=True
        while continuer==True:
            if turtle.exitonclick():
                turtle.bye()
                continuer=False


Labyri=Laby(50,50)
c=Pile()
c.empiler([0,0])
c.empiler([1,0])
c.empiler([2,0])
c.empiler([2,1])
c.empiler([3,1])
c.empiler([4,1])
for l in Labyri.walls:
    print(l)

Labyri.tracage_laby(Labyri.walls,c,10)
