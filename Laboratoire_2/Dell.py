from ast import Pass
import threading
from time import sleep
import grovepi

class Dell:
    def __init__(self , port , sonar , direction):
        self.port = port
        self.sonar = sonar
        self.direction = direction
        self.thread = threading.Thread(target = self.clignoter , args=())
        self.distance_courante = 0
    def __allumez__(self):
        grovepi.digitalWrite(self.port,1)

    def __eteindre__(self):
        grovepi.digitalWrite(self.port,0)
    def __choisir_intensite__(self , valeur):
        grovepi.analogWrite(self.port,valeur)
    def clignoter(self):
        
        
        
        while(not self.arreter):
            
            self.__allumez__()
            sleep(self.calculer_incrementation(self.direction))
            self.__eteindre__()
            
    def calculer_incrementation(direction):
        
        if(direction == 'g'):
            pass
        elif(direction == 'd'):
            pass

        pass

            