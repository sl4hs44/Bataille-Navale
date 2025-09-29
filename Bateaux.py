
class Bateau():
    def __init__(self, vie, positionX, positionY, orientation):
        self.vie = vie                                      
        self.vie_init = vie                                                     # necessaire à l'affichage en bas des différents navires
        self.Xposition = positionX
        self.Yposition = positionY
        self.orientation = orientation   
        self.dico_pos = {}                                                      # dico de positions du navires pour un utilisation dans le test de game.grille.est_touche(arg*)
        
        # Generation des différentes coordonnées du navire
        for k in range(vie):
            if orientation == 'horizontal':
                cle = str(self.Xposition)+';'+str(self.Yposition+k)
                self.dico_pos[cle] = ''
            else:
                cle = str(self.Xposition+k)+';'+str(self.Yposition )
                self.dico_pos[cle] = ''

