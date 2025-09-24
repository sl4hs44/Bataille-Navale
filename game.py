from grille import Grille
import pygame

class Game():
    def __init__(self):
        self.grilleJ1 = Grille()
        self.grilleJ2 = Grille()

        self.EAU = (0, 105, 148)
        self.BATEAU = (169, 169, 169)
        self.TOUCHE = (255, 0, 0)
        self.RATE = (255, 255, 255)


        pygame.init()
        self.taille_case = 100
        self.grille_taille = 10
        self.largeur = self.hauteur = self.taille_case *  self.grille_taille
        self.screen = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Bataille Navale")


    def dessiner_grille(self):
        for i in range( self.grille_taille):
            for j in range( self.grille_taille):
                couleur =  self.EAU
                if  self.grilleJ1[i][j] == 'B':
                    couleur = self.BATEAU
                elif  self.grilleJ1[i][j] == 'X':
                    couleur =  self.TOUCHE
                elif  self.grilleJ1[i][j] == 'O':
                    couleur =  self.RATE
                pygame.draw.rect( self.screen, couleur, (j* self.taille_case, i* self.taille_case, self.taille_case,  self.taille_case))
                pygame.draw.rect( self.screen, (0,0,0), (j* self.taille_case, i* self.taille_case, self.taille_case, self.taille_case), 1)