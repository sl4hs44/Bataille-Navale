import pygame
import sys

class Grille():
    def __init__(self, taille):
        self.taille = taille
        self.matrice = [[0 for k in range(taille)] for k in range(taille)]

        self.EAU = (0, 105, 148)
        self.BATEAU = (169, 169, 169)
        self.TOUCHE = (255, 0, 0)
        self.RATE = (255, 255, 255)

        

        