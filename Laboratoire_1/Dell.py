import threading
from time import sleep
import grovepi

class Dell:
    def __init__(self , port , ):
        self.port = port
        self.thread = threading.Thread(target = self.clignoter , args=())

    def __allumez__(self):
        grovepi.digitalWrite(self.port,1)

    def __eteindre__(self):
        grovepi.digitalWrite(self.port,0)
    def __choisir_intensite__(self , valeur):
        grovepi.analogWrite(self.port,valeur)
    def clignoter(self):
        pass