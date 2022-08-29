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
    def __allumez__(self):
        grovepi.digitalWrite(self.port,1)

    def __eteindre__(self):
        grovepi.digitalWrite(self.port,0)
    def __choisir_intensite__(self , valeur):
        grovepi.analogWrite(self.port,valeur)
    def clignoter(self):
        incrementation = 0
        if(self.direction == 'g'):
            incrementation = self.calculer_incrementation(self.sonar.distance_courante_gauche)
        if(self.direction == 'd'):
            incrementation = self.calculer_incrementation(self.sonar.distance_courante_droite)
        while(not self.arreter):
            self.__allumez__()
            sleep(incrementation)
            self.__eteindre__()
            
    def calculer_incrementation(distance):
        if(distance is None):
            pass 
        pass
    
            