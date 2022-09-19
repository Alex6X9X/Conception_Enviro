import threading
from time import sleep
import gpiozero

DISTANCE_PAR_TRANSITION = 0.6105
class Odomètre:
    def __init__(self , port_out_gauche, port_out_droite):
        self.encodeur_gauche = gpiozero.DigitalInputDevice(port_out_gauche)
        self.encodeur_droite = gpiozero.DigitalInputDevice(port_out_droite)
        self.stop = threading.Event()
        self.nombre_transition = 0
        self.distance_voulue = None
        self.distance = 0

    def avancer_distance(self,distance_voulue):
        ##installer callbacks avant de faire avancer
        self.distance_voulue = distance_voulue
        self.encodeur_gauche.when_activated = self.when_activated_deactivated_gauche
        self.encodeur_gauche.when_deactivated = self.when_activated_deactivated_gauche
        self.encodeur_droite.when_activated = self.when_activated_deactivated_droite
        self.encodeur_droite.when_deactivated = self.when_activated_deactivated_droite


    def when_activated_deactivated_gauche(self):
        self.nombre_transition += 1

        if(self.calculer_distance() >= self.distance_voulue):
            self.stop.set()
        
    def when_activated_deactivated_droite(self):
        self.nombre_transition += 1
    
        if(self.calculer_distance() >= self.distance_voulue):
            self.stop.set()

    def attendre(self):
        self.stop.wait()
        self.encodeur_gauche.when_activated = None
        self.encodeur_gauche.when_deactivated = None
        self.encodeur_droite.when_activated = None
        self.encodeur_droite.when_deactivated = None
        if(self.distance > self.distance_voulue):
            print("Constante trop petite")
        elif(self.distance < self.distance_voulue):
            print("Constante trop grande")
        
    def calculer_distance(self):
        distance = ((self.nombre_transition) /2) * DISTANCE_PAR_TRANSITION
        self.distance = distance
        print(distance)
        return distance

        