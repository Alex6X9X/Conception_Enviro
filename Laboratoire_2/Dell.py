#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

from dis import dis
import threading
from time import sleep
import gpiozero

TRANCHE_CLIGNOTEMENT = 0.01
DETECTION_MINIMUM_SONAR = 20
DETECTION_MAXIMUM_SONAR = 400

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
        
    def Clignoter(self):
        
        while(not self.arreter):
            self.__allumez__()
            sleep(self.__calculer_incrementation__())
            self.__eteindre__()
            sleep(self.__calculer_incrementation__())
            
            
    def __calculer_incrementation__(self):
        if(self.direction == 'g'):
            distance = self.sonar.distance_courante_gauche
            
            if(distance == None):
                distance = 0
            if(distance < DETECTION_MINIMUM_SONAR):
                distance = DETECTION_MINIMUM_SONAR
            return distance * TRANCHE_CLIGNOTEMENT if distance != 0 and distance > DETECTION_MAXIMUM_SONAR else 1
        
        elif(self.direction == 'd'):
            distance = self.sonar.distance_courante_droite
            
            if(distance == None):  
                distance = 0
            if(distance < DETECTION_MINIMUM_SONAR):
                distance = DETECTION_MINIMUM_SONAR
            return distance * TRANCHE_CLIGNOTEMENT if distance != 0 and distance > DETECTION_MAXIMUM_SONAR else 1

        # Si il n'y aucune distinction entre le sonar de droite ou de gauche (Cas extrême)
        return -1


            