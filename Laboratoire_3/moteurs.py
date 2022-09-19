#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022
#Dernier changement le 25 août 2022

import gpiozero

TAUX_VITESSE = 0.1

class Moteurs:
    
    def __init__(self):
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)  # moteur G
        self.ENA = gpiozero.PWMOutputDevice(13)

        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14) # moteur D
        self.ENB = gpiozero.PWMOutputDevice(18)
        
    def avancer(self, dir):
        self.arreter()
        self.IN1.on()
        self.IN3.on()
    
        if(dir == None):
            self.ENA.value = 0.7
            self.ENB.value = 0.75
        elif(dir == "g"):
            self.avancer_gauche()
        elif(dir == "d"):
            self.avancer_droite()
    
    def avancer_gauche(self):
        self.IN2.on()
        self.IN3.on()
        self.ENA.value = 0.6
        self.ENB.value = 0.8
    
    def avancer_droite(self):
        self.IN1.on()
        self.IN4.on()
        self.ENA.value = 0.8
        self.ENB.value = 0.6
        
    def reculer(self):
        self.arreter()
        self.IN2.on()
        self.IN4.on()
        self.ENA.value = 1.0
        self.ENB.value = 1.0
            
    def tourner_90(self, dir):
        self.arreter()
            
        if (dir == "g"):
            self.IN2.on()
            self.IN3.on()
            self.ENA.value = 0.5
            self.ENB.value = 0.5
        elif (dir == "d"):
            self.IN1.on()
            self.IN4.on()
            self.ENA.value = 0.5
            self.ENB.value = 0.5

    def arreter(self):
        self.ENA.off()
        self.ENB.off()
        self.IN1.off()
        self.IN2.off()
        self.IN3.off()
        self.IN4.off()
    
    
    #10% == 0.1
    
    def augmenter_Vitesse(self):
        if(self.ENA.value + TAUX_VITESSE < 1):
            self.ENA.value = self.ENA.value + TAUX_VITESSE 
            self.ENB.value = self.ENB.value + TAUX_VITESSE
        
    def diminuer_Vitesse(self):
        if(self.moteurs.ENB.value - TAUX_VITESSE > 0):
            self.ENA.value = self.ENA.value - TAUX_VITESSE
            self.ENB.value = self.ENB.value - TAUX_VITESSE
        

            
    