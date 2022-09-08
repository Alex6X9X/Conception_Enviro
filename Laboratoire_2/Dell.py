#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

import threading
from time import sleep
import gpiozero

TRANCHE_CLIGNOTEMENT = 2 # À chaque 2 cm
TEMPS_CLIGNOTEMENT = 0.1

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
            print("Allume!")
            self.__allumez__()
            sleep(self.__calculer_incrementation__())
            self.__eteindre__()
            sleep(self.__calculer_incrementation__())
            
        self.Arreter()
            
    def __calculer_incrementation__(self):
        
        #self.sonar.distance_courante_gauche
        #self.sonar.distance_courante_droite
        print(self.sonar.distance_courante_gauche)
        if(self.direction == 'g'):
            #print( (self.sonar.distance_courante_gauche / TRANCHE_CLIGNOTEMENT) * TEMPS_CLIGNOTEMENT)
            return (self.sonar.distance_courante_gauche / TRANCHE_CLIGNOTEMENT) * TEMPS_CLIGNOTEMENT
        elif(self.direction == 'd'):
            #print( (self.sonar.distance_courante_droite / TRANCHE_CLIGNOTEMENT) * TEMPS_CLIGNOTEMENT)
            return (self.sonar.distance_courante_droite / TRANCHE_CLIGNOTEMENT) * TEMPS_CLIGNOTEMENT

        # Si il n'y aucune distinction entre le sonar de droite ou de gauche
        return -1


            