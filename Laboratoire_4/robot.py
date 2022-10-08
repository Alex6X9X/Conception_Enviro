#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 22 septembre 2022

from moteurs import Moteurs

class Robot:
    def __init__(self , camera):
        self.moteurs = Moteurs()
        self.camera = camera
        
    def DeterminerMouvement(self):
        mouvement = self.camera._determiner_position_()
        
        if(mouvement == "droite"):
            self.Avancer_Droite
        elif(mouvement == "gauche"):
            self.Avancer_Gauche
        elif(mouvement == "avancer"):
            self.Avancer()
        else:
            self.Freiner()
    

    def Avancer(self, dir = None):
        self.moteurs.avancer(dir)
        
    def Avancer_Droite(self):
        self.moteurs.avancer_droite
        
    def Avancer_Gauche(self):
        self.moteurs.avancer_gauche
        
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