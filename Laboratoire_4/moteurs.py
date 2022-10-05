#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 22 septembre 2022

import gpiozero

PORT_IN1 = 6
PORT_IN2 = 5
PORT_ENA = 13
PORT_IN3 = 15
PORT_IN4 = 14
PORT_ENB = 18
TAUX_VITESSE = 0.1

class Moteurs:
    
    def __init__(self):
        self.IN1 = gpiozero.DigitalOutputDevice(PORT_IN1)
        self.IN2 = gpiozero.DigitalOutputDevice(PORT_IN2)  # moteur G
        self.ENA = gpiozero.PWMOutputDevice(PORT_ENA)

        self.IN3 = gpiozero.DigitalOutputDevice(PORT_IN3)
        self.IN4 = gpiozero.DigitalOutputDevice(PORT_IN4) # moteur D
        self.ENB = gpiozero.PWMOutputDevice(PORT_ENB)
        
    def avancer(self, dir):
        self.arreter()
        self.IN1.on()
        self.IN3.on()
    
        if(dir == None):
            self.ENA.value = 0.4
            self.ENB.value = 0.4
        elif(dir == "g"):
            self.avancer_gauche()
        elif(dir == "d"):
            self.avancer_droite()
    
    def avancer_gauche(self):
        self.IN2.on()
        self.IN3.on()
        self.ENA.value = 0.4
        self.ENB.value = 0.6
    
    def avancer_droite(self):
        self.IN1.on()
        self.IN4.on()
        self.ENA.value = 0.6
        self.ENB.value = 0.4
        
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
    
    def freiner(self):
        self.ENA.on()
        self.ENB.on()
        self.IN1.on()
        self.IN2.on()
        self.IN3.on()
        self.IN4.on()
    
    #10% == 0.1
    
    def augmenter_Vitesse(self):
        if(self.ENA.value + TAUX_VITESSE < 1):
            self.ENA.value = self.ENA.value + TAUX_VITESSE 
            self.ENB.value = self.ENB.value + TAUX_VITESSE
        
    def diminuer_Vitesse(self):
        if(self.moteurs.ENB.value - TAUX_VITESSE > 0):
            self.ENA.value = self.ENA.value - TAUX_VITESSE
            self.ENB.value = self.ENB.value - TAUX_VITESSE
        

            
    