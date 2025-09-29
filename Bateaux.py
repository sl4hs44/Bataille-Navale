
class Bateau():
    def __init__(self, vie, positionX, positionY, orientation):
        self.vie = vie                                      # Le double tir au meme endroit sera bloqué
        self.vie_init = vie
        self.Xposition = positionX
        self.Yposition = positionY
        self.orientation = orientation   
        self.dico_pos = {}
        
        for k in range(vie):
            if orientation == 'horizontale':
                cle = str(self.Xposition + k)+';'+str(self.Yposition)
                self.dico_pos[cle] = ''
            else:
                cle = str(self.Xposition)+';'+str(self.Yposition + k)
                self.dico_pos[cle] = ''



        
    def est_detruit(self):
        pass
