
class Bateau():
    def __init__(self, vie, positionX, positionY, orientation):
        self.vie = vie                                      # Le double tir au meme endroit sera bloqué
        self.Xposition = positionX
        self.Yposition = positionY
        self.orientation = orientation                     
        

    