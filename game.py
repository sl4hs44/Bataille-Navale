from grille import Grille
import pygame
import sys
import random as rd

class Game():
    def __init__(self):
        # Initialisation du joueur
        self.grilleJ1 = Grille()

        # Initialisation Ordi
        self.grilleOrdi = Grille()
        self.hits = []                                                          # liste des cases touchées pour un bateau en cours
        self.tir_direction = None                                               # "horizontal" ou "vertical"

        # Couleur des cases pygames
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
        self.taille_case = 45
        self.grille_taille = 10
        self.largeur = self.taille_case *  self.grille_taille
        self.hauteur = self.largeur + 120
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Bataille Navale")
        self.font = pygame.font.SysFont(None, 28)

        # Zones des boutons
        self.orientation ='horizontal'
        self.btn_h = pygame.Rect(10, self.grille_taille*self.taille_case + 60, 120, 40)
        self.btn_v = pygame.Rect(150, self.grille_taille*self.taille_case + 60, 120, 40)


    def dessiner_grille_dev(self, grille : Grille):
        if grille == self.grilleJ1:                                             # Si c'est la grille joueur, affichage des bateaux
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
        else:                                                                   # Si c'est la grille Ordi, on n'affiche pas les bateaux
            for i in range( self.grille_taille):
                for j in range( self.grille_taille):
                    couleur =  self.EAU
                    if grille.matrice[i][j] == 'B':
                        couleur = self.EAU
                    elif  grille.matrice[i][j] == 'X':
                        couleur =  self.TOUCHE
                    elif  grille.matrice[i][j] == 'O':
                        couleur =  self.RATE
                    pygame.draw.rect( self.screen, couleur, (j* self.taille_case, i* self.taille_case, self.taille_case, self.taille_case))
                    pygame.draw.rect( self.screen, (0,0,0), (j* self.taille_case, i* self.taille_case, self.taille_case, self.taille_case), 1)



    def dessiner_grille_actu(self, grille : Grille):
        # Affichage entier de toutes les différentes informations
        self.screen.fill((0,0,0))
        self.dessiner_grille_dev(grille)
        self.dessiner_indicatif_bateaux(self.grilleJ1, 0)
        self.dessiner_indicatif_bateaux(self.grilleOrdi, 310)
        pygame.display.flip()


    def dessiner_bateau(self, taille):
        # Affichage du bateaux à placer lors de l'initialisation
        texte = self.font.render(f"Bateau à placer ({taille} cases)", True, self.TEXTE)
        self.screen.blit(texte, (310, self.grille_taille*self.taille_case + 17))
        for i in range(taille):
            x = 10 + i*self.taille_case + 300
            y = self.grille_taille*self.taille_case + 40
            pygame.draw.rect(self.screen, self.BATEAU, (x, y, self.taille_case, self.taille_case))
            pygame.draw.rect(self.screen, self.NOIR, (x, y, self.taille_case, self.taille_case), 1)


    def dessiner_boutons(self):
        # Dessin des boutons pour le placement des navires joueurs
        # Bouton Horizontale
        pygame.draw.rect(self.screen, self.GRIS_CLAIR if self.orientation=="horizontal" else self.GRIS, self.btn_h)
        txt_h = self.font.render("Horizontal", True, self.NOIR)
        self.screen.blit(txt_h, (self.btn_h.x+10, self.btn_h.y+10))

        # Bouton Verticale
        pygame.draw.rect(self.screen, self.GRIS_CLAIR if self.orientation=="vertical" else self.GRIS, self.btn_v)
        txt_v = self.font.render("Vertical", True, self.NOIR)
        self.screen.blit(txt_v, (self.btn_v.x+10, self.btn_v.y+10))


    def dessiner_indicatif_bateaux(self, grille: Grille, ecart):
        # Dessine les bateaux en petit en bas --> 'taille' peremet de déplacer selon X l'affichage
        # Cela permet une distinction entre les navires Joueur et ordi
        x_base = 10 + ecart
        y_base = self.grille_taille * self.taille_case + 10

        taille_case_mini = int(self.taille_case * 0.3)                          # 30% de la taille normale
        espacement = 10                                                         # espace horizontal entre bateaux

        for index, bateau in enumerate(grille.liste_bateaux):
            # Couleur selon état
            if bateau in grille.liste_bateaux_detruits:
                couleur = self.TOUCHE                                           # rouge = détruit
            else:                                       
                couleur = self.BATEAU                                           # gris = encore en jeu

            # Position de départ pour ce bateau
            start_x = x_base + index * (taille_case_mini + espacement)
            start_y = y_base

            # Dessiner le bateau sous forme de carrés alignés verticalement
            for i in range(bateau.vie_init):
                x = start_x
                y = start_y + i * (taille_case_mini + 2)                        # aligné verticalement
                pygame.draw.rect(self.screen, couleur, (x, y, taille_case_mini, taille_case_mini))
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, taille_case_mini, taille_case_mini), 1)


    def dessiner_fin(self, index):
        self.screen.fill((0, 0, 0))
        # Choisir le texte et la couleur
        if index == 1:
            message = "Victoire !"
            couleur = (0, 255, 0)                                               # vert
        else:
            message = "Défaite..."
            couleur = (255, 0, 0)                                               # rouge

        font_fin = pygame.font.SysFont(None, 80)
        texte = font_fin.render(message, True, couleur)
        rect = texte.get_rect(center=(self.largeur // 2, self.hauteur // 2))
        self.screen.blit(texte, rect)
        pygame.display.flip()


    def choix_bateaux(self, grille : Grille):
        # Boucle tournant durant la phase de préparation de la grille (positionnement des bateaux joueur)
        possible_position = True
        taille = grille.liste_bateaux_a_placer.pop()
        while taille !=0 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                   # Cas où l'on quitte la fenêtre de jeu
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:                      # Cas où l'on clic sur une case
                    x, y = event.pos
                    if self.btn_h.collidepoint(x, y):
                        self.orientation = "horizontal"
                    elif self.btn_v.collidepoint(x, y):
                        self.orientation = "vertical"
                    elif y < self.grille_taille*self.taille_case:               # Vérification de clic DANS la grille
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


    def tir_auto(self, grille: Grille):
        # mémoriser le nombre de bateaux détruits avant le tir
        nb_detruits_avant = len(grille.liste_bateaux_detruits)

        # choisir la case
        if len(self.hits) == 1:
            ligne, colonne = self.hits[0]
            candidates = []

            for dl, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_l = ligne + dl
                new_c = colonne + dc
                if 0 <= new_l < self.grille_taille and 0 <= new_c < self.grille_taille:
                    if not grille.already_tir(new_l, new_c):
                        candidates.append((new_l, new_c))

            if candidates:
                ligne, colonne = rd.choice(candidates)
                touche = grille.est_touche(ligne, colonne)
                if touche:
                    self.hits.append((ligne, colonne))
            else:
                ligne, colonne = self.tir_aleatoire(grille)
                touche = grille.est_touche(ligne, colonne)
                if touche:
                    self.hits=[(ligne, colonne)]

        elif len(self.hits) > 1:
            # Déduire la direction si on a 2 hits
            if len(self.hits) == 2:
                (l1, c1), (l2, c2) = self.hits[:2]
                self.tir_direction = "horizontal" if l1 == l2 else "vertical"

            # Générer candidates selon direction
            candidates = []
            for l, c in self.hits:
                if self.tir_direction == "horizontal":
                    for dc in [-1, 1]:
                        nc = c + dc
                        if 0 <= nc < self.grille_taille and not grille.already_tir(l, nc):
                            candidates.append((l, nc))
                elif self.tir_direction == "vertical":
                    for dl in [-1, 1]:
                        nl = l + dl
                        if 0 <= nl < self.grille_taille and not grille.already_tir(nl, c):
                            candidates.append((nl, c))
            if candidates:
                ligne, colonne = rd.choice(candidates)
                touche = grille.est_touche(ligne, colonne)
                if touche:
                    self.hits.append((ligne, colonne))
            else:
                ligne, colonne = self.tir_aleatoire(grille)
                touche = grille.est_touche(ligne, colonne)
                if touche:
                    self.hits=[(ligne, colonne)]

        else:
            ligne, colonne = self.tir_aleatoire(grille)
            touche = grille.est_touche(ligne, colonne)
            if touche:
                self.hits.append((ligne, colonne))

        # Vérifier si un nouveau bateau a été détruit
        if len(grille.liste_bateaux_detruits) > nb_detruits_avant:
            # bateau coulé → reset hits et direction
            self.hits = []
            self.tir_direction = None


    def tir_aleatoire(self, grille: Grille):
        ligne = rd.randint(0,self.grille_taille - 1)
        colonne = rd.randint(0,self.grille_taille - 1)
        while grille.already_tir(ligne, colonne):
            ligne = rd.randint(0,self.grille_taille - 1)
            colonne = rd.randint(0,self.grille_taille - 1)
        return ligne, colonne
                