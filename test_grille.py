from grille import Grille


grille1 = Grille()

assert grille1.isnot_over()

grille1.matrice[2][2] = 'X'
assert grille1.already_tir(2,2)
assert not(grille1.already_tir(2,3))


