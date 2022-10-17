#Alexandre Carle et Louis-philippe Rousseau
#Dernier changement le 13 octobre 2022

from moteurs import Moteurs

class Robot:
    def __init__(self , camera):
        self.moteurs = Moteurs()
        self.camera = camera
        
    def DeterminerMouvement(self):
        mouvement = self.camera._determiner_position_()
        
        if(mouvement == "droite"):
            self.Avancer("d")
        elif(mouvement == "gauche"):
            self.Avancer("g")
        elif(mouvement == "avancer"):
            self.Avancer()
        else:
            self.Freiner()

    def Avancer(self, dir = None):
        self.moteurs.avancer(dir)
        
    def Reculer(self):
        self.moteurs.reculer()
            
    def Tourner(self, dir):
        self.moteurs.tourner(dir)

    def Arreter(self):
        self.moteurs.arreter()
        
    def Freiner(self):
        self.moteurs.freiner()
    
    def Augmenter_Vitesse(self):
        self.moteurs.augmenter_Vitesse()
        
    def Diminuer_Vitesse(self):
        self.moteurs.diminuer_Vitesse()