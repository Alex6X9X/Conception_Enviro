#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022
#Dernier changement le 28 août 2022

import gpiozero
from moteurs import Moteurs

class Robot:
    def __init__(self):
        self.moteurs = Moteurs()
        
        
    def Avancer(self, dir = None):
        self.Arreter()
        self.moteurs.IN1.on()
        self.moteurs.IN3.on()
        
        if(dir == None):
            self.moteurs.ENA.value = 1.0
            self.moteurs.ENB.value = 1.0
        elif(dir == "g"):
            self.moteurs.IN2.on()
            self.moteurs.IN3.on()
            self.moteurs.ENA.value = 0.6
            self.moteurs.ENB.value = 0.8
        elif(dir == "d"):
            self.moteurs.IN1.on()
            self.moteurs.IN4.on()
            self.moteurs.ENA.value = 0.8
            self.moteurs.ENB.value = 0.6
        
        
    def Reculer(self):
        self.Arreter()
        self.moteurs.IN2.on()
        self.moteurs.IN4.on()
        self.moteurs.ENA.value = 1.0
        self.moteurs.ENB.value = 1.0
            
    def Tourner_90(self, dir):
        self.Arreter()
            
        if (dir == "g"):
            self.moteurs.IN2.on()
            self.moteurs.IN3.on()
            self.moteurs.ENA.value = 0.5
            self.moteurs.ENB.value = 0.5
        elif (dir == "d"):
            self.moteurs.IN1.on()
            self.moteurs.IN4.on()
            self.moteurs.ENA.value = 0.5
            self.moteurs.ENB.value = 0.5

    def Arreter(self):
        self.moteurs.ENA.off()
        self.moteurs.ENB.off()
        self.moteurs.IN1.off()
        self.moteurs.IN2.off()
        self.moteurs.IN3.off()
        self.moteurs.IN4.off()
    
    
    #10% == 0.1
    
    def Augmenter_Vitesse(self):
        if(self.moteurs.ENA.value + 0.1 < 1):
            self.moteurs.ENA.value = self.moteurs.ENA.value + 0.1 
            self.moteurs.ENB.value = self.moteurs.ENB.value + 0.1
        
    def Diminuer_Vitesse(self):
        if(self.moteurs.ENB.value - 0.1 > 0):
            self.moteurs.ENA.value = self.moteurs.ENA.value - 0.1
            self.moteurs.ENB.value = self.moteurs.ENB.value - 0.1