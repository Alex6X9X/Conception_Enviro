#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 22 septembre 2022

from moteurs import Moteurs

class Robot:
    def __init__(self):
        self.moteurs = Moteurs()
        
        
    def Avancer(self, dir = None):
        self.moteurs.avancer(dir)
        
        
    def Reculer(self):
        self.moteurs.reculer()
            
    def Tourner_90(self, dir):
        self.moteurs.tourner_90(dir)

    def Arreter(self):
        self.moteurs.arreter()
        
    def Freiner(self):
        self.moteurs.freiner()
    
    def Augmenter_Vitesse(self):
        self.moteurs.augmenter_Vitesse()
        
    def Diminuer_Vitesse(self):
        self.moteurs.diminuer_Vitesse()