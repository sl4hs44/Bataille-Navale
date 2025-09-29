from game import Game
import pygame
import sys
import time


game = Game()                                                                   # Initialisation de la partie

game.choix_bateaux(game.grilleJ1)                                               # Partie positionnement des bateaux Joueurs
game.grilleOrdi.positionnement_bateaux_aleatoire()                              # Positionnement automatique et aléatoire du bateaux Ordi





game.dessiner_grille_actu(game.grilleJ1)                                        # Afficahge grille Joueur complète
time.sleep(1)
game.dessiner_grille_actu(game.grilleOrdi)                                      # Affichage grille Ordi pour jeu


runJ1 = True                                                                    # Variables indicatrices de défaites/victoires
runOrdi = True
while runJ1 and runOrdi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                           # Cas où l'on quitte la fenêtre
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:                              # Cas d'un clic
            x, y = event.pos
            ligne = y // game.taille_case
            colonne = x // game.taille_case
            # Exemple : marquer un tir
            if not(game.grilleOrdi.already_tir(ligne, colonne)):                # Vérification de x et y (DANS la grille et pas déjà sur une case tirée)
                game.grilleOrdi.est_touche(ligne, colonne)
            else:
                break                                                           # Si la vérification échou, alors il y a le clic n'est pas comptabilisé

            # Rafraîchir uniquement après le clic
            game.dessiner_grille_actu(game.grilleOrdi)
        
            # Début du tour automatique de l'ordi
            time.sleep(0.5)                                 
            game.dessiner_grille_actu(game.grilleJ1)
            time.sleep(0.2)
            game.tir_auto(game.grilleJ1)
            game.dessiner_grille_actu(game.grilleJ1)
            time.sleep(1)
            # Début du tour du joueur
            game.dessiner_grille_actu(game.grilleOrdi)
            

            # Test de fin de boucle
            runJ1 = game.grilleJ1.isnot_over()
            runOrdi = game.grilleOrdi.isnot_over()



if runOrdi:                                                                     # Affichage victoire ou défaite
    game.dessiner_fin(0)
else:
    game.dessiner_fin(1)
              
while True:                                                                     # Permet que la fenêtre reste ouverte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
