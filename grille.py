from Bateaux import Bateau
import random as rd

class Grille():
    def __init__(self):
        self.taille = 10
        self.matrice = [['~' for k in range(self.taille)] for k in range(self.taille)]

        self.liste_bateaux_a_placer = [0, 5, 4, 3, 3, 2]                        # 0 permet de quitter la boucle de paramétrage (positionnement des bateaux)
        self.liste_bateaux = []
        self.liste_bateaux_detruits = []


    def est_touche(self, x,y):
        if self.matrice[x][y] == 'B':
            self.matrice[x][y] = 'X'                                           # touché
            for boat in self.liste_bateaux:
                cle = str(x)+';'+str(y)
                if cle in boat.dico_pos:
                    boat.vie -= 1
                    if boat.vie == 0:
                        self.liste_bateaux_detruits.append(boat)
            return True
        elif self.matrice[x][y] == '~':
            self.matrice[x][y] = 'O'                                           # raté
            return False
        
    def positionnement_bateaux(self, ligne, colonne, taille, orientation):
        if orientation == "horizontal":
            if colonne + taille > self.taille: return False
            for i in range(taille):
                if self.matrice[ligne][colonne+i] != '~': return False
            for i in range(taille):
                self.matrice[ligne][colonne+i] = 'B'
            self.liste_bateaux.append(Bateau(taille, ligne, colonne, orientation))
        else:
            if ligne + taille > self.taille: return False
            for i in range(taille):
                if self.matrice[ligne+i][colonne] != '~': return False
            for i in range(taille):
                self.matrice[ligne+i][colonne] = 'B'
            self.liste_bateaux.append(Bateau(taille, ligne, colonne, orientation))
        return True
    

    def positionnement_bateaux_aleatoire(self):
        pass
    
    