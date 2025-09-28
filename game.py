from grille import Grille
import pygame

class Game():
    def __init__(self):
        # Initialisation des Joueurs
        self.grilleJ1 = Grille()


        self.EAU = (0, 105, 148)
        self.BATEAU = (169, 169, 169)
        self.TOUCHE = (255, 0, 0)
        self.RATE = (255, 255, 255)

        # Generation de la grille pour le visuel
        pygame.init()
        self.taille_case = 60
        self.grille_taille = 10
        self.largeur = self.taille_case *  self.grille_taille
        self.hauteur = self.largeur + self.taille_case
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Bataille Navale")


    def dessiner_grille_dev(self, grille : Grille):                     # Dessiner 'DEV' car elle montre la position des bateaux
        self.screen.fill((0,0,0))
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
        pygame.display.flip()

    def dessiner_bateau_courant():
        if index_bateau < len(bateaux):
            taille = bateaux[index_bateau]
            texte = font.render(f"Bateau à placer ({taille} cases)", True, TEXTE)
            screen.blit(texte, (10, grille_taille*taille_case + 10))
            for i in range(taille):
                x = 10 + i*taille_case
                y = grille_taille*taille_case + 30
                pygame.draw.rect(screen, BATEAU, (x, y, taille_case, taille_case))
                pygame.draw.rect(screen, NOIR, (x, y, taille_case, taille_case), 1)
    
    def choix_bateaux(self, grille : Grille):
        self.dessiner_grille_dev()
        run_posi = True
        while run_posi:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    ligne = y // self.taille_case
                    colonne = x // self.taille_case

                    grille.positionnement_bateaux(self, x, y, )



                