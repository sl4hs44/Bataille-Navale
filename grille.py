import pygame
import sys
from Bateaux import Bateau

class Grille():
    def __init__(self):
        self.taille = 10
        self.matrice = [['~' for k in range(self.taille)] for k in range(self.taille)]

        self.liste_bateaux_a_placer= [5, 4, 3, 3, 2]



    def est_touche(self, x,y):
        if self.matrice[x][y] == 'B':
            self.matrice[x][y] = 'X'                                           # touché
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
        else:
            if ligne + taille > self.taille: return False
            for i in range(taille):
                if self.matrice[ligne+i][colonne] != '~': return False
            for i in range(taille):
                self.matrice[ligne+i][colonne] = 'B'
        return True
    
    
    def dessiner_bateau(self):
        taille = self.liste_bateaux_a_placer.pop()
        texte = font.render(f"Bateau à placer ({taille} cases)", True, TEXTE)
        screen.blit(texte, (10, grille_taille*taille_case + 10))
        for i in range(taille):
            x = 10 + i*taille_case
            y = grille_taille*taille_case + 30
            pygame.draw.rect(screen, BATEAU, (x, y, taille_case, taille_case))
            pygame.draw.rect(screen, NOIR, (x, y, taille_case, taille_case), 1)