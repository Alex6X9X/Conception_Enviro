from moteurs import Moteurs
class Robot :
    def __init__(self):
        self.moteurs = Moteurs()
        self.x = 0
        self.y = 0
        
    def Avancer(self):
        self.moteurs.avancer()
        
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