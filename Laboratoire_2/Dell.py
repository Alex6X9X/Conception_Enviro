#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

import threading
from time import sleep
import gpiozero

TRANCHE_CLIGNOTEMENT = 2 # À chaque 2 cm
TEMPS_CLIGNOTEMENT = 0.01

class Dell:
    def __init__(self , port , sonar , direction, arreter):
        self.sonar = sonar
        self.direction = direction
        self.thread = threading.Thread(target = self.Clignoter , args=())
        self.arreter = arreter
        self.dell = gpiozero.DigitalOutputDevice(port)
        
    def Demarrer(self):
        self.thread.start()
        
    def Arreter(self):
        self.thread.join()
        
    def __allumez__(self):
        self.dell.on()

    def __eteindre__(self):
        self.dell.off()
        
    def Clignoter(self, distance_g, distance_d):
        
        while(not self.arreter):
            
            self.__allumez__()
            sleep(self.__calculer_incrementation__(20, 25))
            self.__eteindre__()
            
        self.Arreter()
            
    def __calculer_incrementation__(self, distance_g, distance_d):
        
        if(self.direction == 'g'):
            return (distance_g / TRANCHE_CLIGNOTEMENT) * TEMPS_CLIGNOTEMENT
        elif(self.direction == 'd'):
            return (distance_d / TRANCHE_CLIGNOTEMENT)

        # Si il n'y aucune distinction entre le sonar de droite ou de gauche
        return -1


            