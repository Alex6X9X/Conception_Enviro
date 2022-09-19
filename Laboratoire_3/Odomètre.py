import threading
from time import sleep
import gpiozero

DISTANCE_PAR_TRANSITION=0.55
class Odomètre:
    def __init__(self , port_out_gauche, port_out_droite):
        self.encodeur_gauche = gpiozero.DigitalInputDevice(port_out_gauche)
        self.encodeur_droite = gpiozero.DigitalInputDevice(port_out_droite)
        self.stop = threading.Event()
        self.nombre_transition_gauche =0
        self.nombre_transition_droite =0
        pass
    def avancer_distance(self,distance_voulue):
        ##installer callbacks avant de faire avancer

        self.encodeur_gauche.when_activated = self.when_activated_gauche
        self.encodeur_gauche.when_deactivated = self.when_deactivated_gauche
        self.encodeur_droite.when_activated = self.when_activated_droite
        self.encodeur_droite.when_deactivated = self.when_deactivated_droite
        if(self.calculer_distance() == distance_voulue):
            self.stop.set()
        pass
    def when_activated_gauche(self):
        print(self.nombre_transition_droite)
        print(self.nombre_transition_gauche)
        self.nombre_transition_gauche += 1
    def when_deactivated_gauche(self):
        self.nombre_transition_gauche += 1
    def when_activated_droite(self):
        self.nombre_transition_droite += 1
    def when_deactivated_droite(self):
        self.nombre_transition_droite += 1
        
    def attendre(self):
        self.stop.wait()
        self.encodeur_gauche.when_activated = None
        self.encodeur_gauche.when_deactivated = None
        self.encodeur_droite.when_activated = None
        self.encodeur_droite.when_deactivated = None
        
    def calculer_distance(self):
        distance = ((self.nombre_transition_gauche + self.nombre_transition_droite) /2) * DISTANCE_PAR_TRANSITION
        return distance

        