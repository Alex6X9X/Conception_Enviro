#Auteurs: Alexandre Carle et Louis-philippe Rousseau et Guillaume Légaré
#Dernier changement 10 novembre 2022
from State import State
from moteurs import Moteurs
class Robot :
    def __init__(self, navigation , radioNavigation):
        self.moteurs = Moteurs()
        self.navigation = navigation
        self.radioNavigation = radioNavigation
        self.x = 0
        self.y = 0
        
    def Avancer(self):
        self.navigation.état = State.Translation
        self.moteurs.avancer()
    def AvancerX(self , positionToGoTo):
        
        while(self.radioNavigation.x):
            pass
        self.navigation.état = State.Translation
    
    

    def Reculer(self):
        self.navigation.état = State.Translation
        self.moteurs.reculer()
            
    def Tourner(self, dir):
        self.navigation.état = State.Rotation
        self.moteurs.tourner(dir)

    def Arreter(self):
        self.moteurs.arreter()
        self.navigation.état = State.Immobile
        
    def Freiner(self):
        self.moteurs.freiner()
        self.navigation.état = State.Immobile
    