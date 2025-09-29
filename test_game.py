from game import Game
import pygame
import sys
import time


game = Game()

game.choix_bateaux(game.grilleJ1)
game.grilleOrdi.positionnement_bateaux_aleatoire()





game.dessiner_grille_actu(game.grilleJ1)
game.dessiner_grille_actu(game.grilleOrdi)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            ligne = y // game.taille_case
            colonne = x // game.taille_case
            # Exemple : marquer un tir

            game.grilleOrdi.est_touche(ligne, colonne)

            # Rafraîchir uniquement après le clic
            game.dessiner_grille_actu(game.grilleOrdi)
        
            time.sleep(0.5)
            game.dessiner_grille_actu(game.grilleJ1)
            time.sleep(1)
            game.dessiner_grille_actu(game.grilleOrdi)

            
            
