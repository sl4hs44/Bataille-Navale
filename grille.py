import pygame
import sys

class Grille():
    def __init__(self):
        self.taille = 10
        self.matrice = [[0 for k in range(self.taille)] for k in range(self.taille)]



        