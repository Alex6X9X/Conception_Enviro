#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 19 septembre 2022

import threading
import gpiozero

DISTANCE_PAR_TRANSITION = 0.60 #Ne pas changer (Tests effectues)
class Odomètre:
    def __init__(self , port_out_gauche, port_out_droite):
        self.encodeur_gauche = gpiozero.DigitalInputDevice(port_out_gauche)
        self.encodeur_droite = gpiozero.DigitalInputDevice(port_out_droite)
        self.stop = threading.Event()
        self.nombre_transition = 0
        self.distance_voulue = None
        self.lock = threading.Lock()

    def avancer_distance(self,distance_voulue):
        self.distance_voulue = distance_voulue
        self.encodeur_gauche.when_activated = self.when_activated_deactivated
        self.encodeur_gauche.when_deactivated = self.when_activated_deactivated
        self.encodeur_droite.when_activated = self.when_activated_deactivated
        self.encodeur_droite.when_deactivated = self.when_activated_deactivated


    def when_activated_deactivated(self):
        with self.lock:
            self.nombre_transition += 1
        if(self.calculer_distance() >= self.distance_voulue):
            self.stop.set()

    def attendre(self):
        self.stop.wait()
        self.encodeur_gauche.when_activated = None
        self.encodeur_gauche.when_deactivated = None
        self.encodeur_droite.when_activated = None
        self.encodeur_droite.when_deactivated = None
        
    def calculer_distance(self):
        distance = (self.nombre_transition / 2) * DISTANCE_PAR_TRANSITION
        return distance

        