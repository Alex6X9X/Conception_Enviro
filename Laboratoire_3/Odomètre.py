import threading
from time import sleep
import gpiozero
from symbol import pass_stmt
DISTANCE_PAR_TRANSITION=22
class Odomètre:
    def __init__(self , port_out_gauche, port_out_droite):
        self.encodeur_gauche = gpiozero.DigitalInputDevice(port_out_gauche)
        self.encodeur_droite = gpiozero.DigitalInputDevice(port_out_droite)
        pass
    def avancer_distance(self,distance):
        ##installer callbacks avant de faire avancer

        pass
    def when_activated_gauche(self):
        pass
    def when_deactivated_gauche(self):
        pass
    def when_activated_droite(self):
        pass
    def when_deactivated_droite(self):
        pass
    def attendre(self):
        pass

        