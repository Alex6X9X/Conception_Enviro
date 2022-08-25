#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022

import gpiozero
from moteurs import Moteurs

class Robot:
    def __init__(self):
        self.moteurs = Moteurs();
        
        
    def Avancer(self, dir):
        self.Arreter()
        self.moteurs.IN1.on()
        self.moteurs.IN3.on()
        
        if(dir == None or dir == " "):
            self.moteurs.ENA.value = 0.3
            self.moteurs.ENB.value = 0.3
        elif(dir == "g"):
            self.moteurs.ENA.value = 0.1
            self.moteurs.ENB.value = 0.4
        elif(dir == "d"):
            self.moteurs.ENA.value = 0.4
            self.moteurs.ENB.value = 0.1
        
        
    def Reculer(self):
        self.Arreter()
        self.moteurs.IN2.on()
        self.moteurs.IN4.on()
        self.moteurs.ENA.value = 0.3
        self.moteurs.ENB.value = 0.3
            
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
        self.moteurs.ENA.value = self.moteurs.ENA.value + 0.1 
        self.moteurs.ENB.value = self.moteurs.ENA.value + 0.1
        print(self.moteurs.ENB.value)
        print(self.moteurs.ENA.value)
        
    def Diminuer_Vitesse(self):
        self.moteurs.ENA.value -= 0.1
        self.moteurs.ENB.value -= 0.1
        print(self.moteurs.ENB.value)
        print(self.moteurs.ENA.value)