from game import Game
from grille import Grille
import pygame
import sys
import time


game = Game()                                                                   # Permet d'avoir un affichage visuel du resultat du test

# Faire un test de position automatique avec répétition : grille.positionnement_bateaux_aléatoire
# Le positionnement aléatoire utilise les fonctions de positionnements classiques et la vérification
for k in range(40):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                           # Cas où l'on quitte la fenêtre
            pygame.quit()
            sys.exit()
    game.grilleJ1.positionnement_bateaux_aleatoire()                          # Position aléatoire de bateaux
    game.screen.fill((0,0,0))
    game.dessiner_grille_dev(game.grilleJ1)
    pygame.display.flip()
    time.sleep(2)
    game.grilleJ1 = Grille()                                                  # Réinitialisation de Grille

