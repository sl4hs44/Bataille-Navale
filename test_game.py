from game import Game
import pygame
import sys


game = Game()

#game.choix_bateaux(game.grilleJ1)
game.grilleJ1.positionnement_bateaux_aleatoire()




game.dessiner_grille_actu(game.grilleJ1)
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

            game.grilleJ1.est_touche(ligne, colonne)

            # Rafraîchir uniquement après le clic
            game.dessiner_grille_actu(game.grilleJ1)
            
            
