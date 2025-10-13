from grille import Grille
from game import Game
import time

grille1 = Grille()

# Essaie de fin de jeu
assert grille1.isnot_over()


# test de vérification de tir possible
grille1.matrice[2][2] = 'X'
assert grille1.already_tir(2,2)
assert not(grille1.already_tir(2,3))


# Test des postionnements du bateaux
grille1.positionnement_bateaux(3, 3, 2, 'horizontal')
assert grille1.matrice[3][3] == 'B'
assert grille1.matrice[4][3] == '~'                                             # Il y a une inversion car je fonctionne en ligne(y) colonne(x) partout sauf ici ou j'utilise X et y
assert grille1.matrice[3][4] == 'B'

# Test de tir 
assert not(grille1.est_touche(4,3))
assert grille1.est_touche(3,3)
assert grille1.est_touche(3,4)                                                  # Un bateau détruit sera ajouté à la liste bateaux détruit

for k in range(0,4):
    grille1.liste_bateaux_detruits.append(1)                                    # Ajout d'objet dans la liste bateaux détruits

assert not(grille1.isnot_over())                                                # Détecte s'il y a 5 elements dans la liste bateaux détruits











