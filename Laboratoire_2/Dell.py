#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

import threading
from time import sleep
import gpiozero

TRANCHE_CLIGNOTEMENT = 0.007
DETECTION_MINIMUM_SONAR = 2
DETECTION_MAXIMUM_SONAR = 400
TEMPS_MAXIMUM = 4.0

class Dell:
    def __init__(self , port, sonar, arreter):
        self.sonar = sonar
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
            sleep(self.__calculer_sleep__())
            self.__eteindre__()
            sleep(self.__calculer_sleep__())
            
            
    def __calculer_sleep__(self):
        distance = self.sonar.distance_courante
        
        if(distance == None):
            return TEMPS_MAXIMUM
        if(distance < DETECTION_MINIMUM_SONAR):
            distance = DETECTION_MINIMUM_SONAR
        return distance * TRANCHE_CLIGNOTEMENT if distance < DETECTION_MAXIMUM_SONAR else TEMPS_MAXIMUM
    



            