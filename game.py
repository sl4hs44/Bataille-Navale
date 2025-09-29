from grille import Grille
import pygame
import sys

class Game():
    def __init__(self):
        # Initialisation des Joueurs
        self.grilleJ1 = Grille()


        self.EAU = (0, 105, 148)
        self.BATEAU = (169, 169, 169)
        self.TOUCHE = (255, 0, 0)
        self.RATE = (255, 255, 255)
        self.TEXTE = (255, 255, 255)
        self.GRIS = (100, 100, 100)
        self.GRIS_CLAIR = (180, 180, 180)
        self.NOIR = (255, 255, 255)

        # Generation de la grille pour le visuel
        pygame.init()
        self.taille_case = 60
        self.grille_taille = 10
        self.largeur = self.taille_case *  self.grille_taille
        self.hauteur = self.largeur + 120
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Bataille Navale")
        self.font = pygame.font.SysFont(None, 28)

        # Zones des boutons
        self.orientation ='horizontale'
        self.btn_h = pygame.Rect(10, self.grille_taille*self.taille_case + 60, 120, 40)
        self.btn_v = pygame.Rect(150, self.grille_taille*self.taille_case + 60, 120, 40)


    def dessiner_grille_dev(self, grille : Grille):                     # Dessiner 'DEV' car elle montre la position des bateaux
        for i in range( self.grille_taille):
            for j in range( self.grille_taille):
                couleur =  self.EAU
                if grille.matrice[i][j] == 'B':
                    couleur = self.BATEAU
                elif  grille.matrice[i][j] == 'X':
                    couleur =  self.TOUCHE
                elif  grille.matrice[i][j] == 'O':
                    couleur =  self.RATE
                pygame.draw.rect( self.screen, couleur, (j* self.taille_case, i* self.taille_case, self.taille_case,  self.taille_case))
                pygame.draw.rect( self.screen, (0,0,0), (j* self.taille_case, i* self.taille_case, self.taille_case, self.taille_case), 1)
        

    def dessiner_grille_actu(self, grille : Grille):
        self.screen.fill((0,0,0))
        self.dessiner_grille_dev(grille)
        pygame.display.flip()

    def dessiner_bateau(self, taille):
            texte = self.font.render(f"Bateau à placer ({taille} cases)", True, self.TEXTE)
            self.screen.blit(texte, (310, self.grille_taille*self.taille_case + 17))
            for i in range(taille):
                x = 10 + i*self.taille_case + 300
                y = self.grille_taille*self.taille_case + 40
                pygame.draw.rect(self.screen, self.BATEAU, (x, y, self.taille_case, self.taille_case))
                pygame.draw.rect(self.screen, self.NOIR, (x, y, self.taille_case, self.taille_case), 1)


    def dessiner_boutons(self):
        # Bouton Horizontale
        pygame.draw.rect(self.screen, self.GRIS_CLAIR if self.orientation=="horizontal" else self.GRIS, self.btn_h)
        txt_h = self.font.render("Horizontale", True, self.NOIR)
        self.screen.blit(txt_h, (self.btn_h.x+10, self.btn_h.y+10))

        # Bouton Verticale
        pygame.draw.rect(self.screen, self.GRIS_CLAIR if self.orientation=="vertical" else self.GRIS, self.btn_v)
        txt_v = self.font.render("Verticale", True, self.NOIR)
        self.screen.blit(txt_v, (self.btn_v.x+10, self.btn_v.y+10))



    def choix_bateaux(self, grille : Grille):
        possible_position = True
        taille = grille.liste_bateaux_a_placer.pop()
        while taille !=0 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.btn_h.collidepoint(x, y):
                        self.orientation = "horizontal"
                    elif self.btn_v.collidepoint(x, y):
                        self.orientation = "vertical"
                    elif y < self.grille_taille*self.taille_case:                       # clic dans la grille
                        if taille != 0:
                            ligne = y // self.taille_case
                            colonne = x // self.taille_case
                            possible_position = grille.positionnement_bateaux(ligne, colonne, taille, self.orientation)
                            if possible_position:
                                taille = grille.liste_bateaux_a_placer.pop()



            # Affichage
            self.screen.fill((0,0,0))
            self.dessiner_grille_dev(grille)
            self.dessiner_bateau(taille)
            self.dessiner_boutons()
            pygame.display.flip()



                