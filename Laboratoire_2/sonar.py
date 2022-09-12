#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 12 septembre 2022

import threading
import gpiozero
import time 
from calculer_moyenne_mobile import calculer_moyenne_mobile

FENETRE = 10
TEMPS_TRIGGER_ACTIF = 0.000001
VITESSE_SON = 343
CONVERSION_CM = 100

class Sonar:
    
    def __init__(self , port_trigger , port_echo, arreter):
        
        #Sonars
        self.trigger = gpiozero.DigitalOutputDevice(port_trigger)
        self.echo = gpiozero.DigitalInputDevice(port_echo)
        self.temps_inactif = 0
        self.temps_actif = 0
        
        self.thread = threading.Thread(target = self.envoyer_ondes , args=())
        
        #Distances
        self.compteur_distance = 0

        self.distance_courante = 0

        self.tableau_distance = []
        
        #Booléen pour l'arrêt du programme
        self.arreter = arreter
        
        self.initialiser_callbacks()
        
    def Demarrer(self):
        self.thread.start()
        
    def Arreter(self):
        self.thread.join()

    def initialiser_callbacks(self):
        self.echo.when_activated = self.sonar_activer
        self.echo.when_deactivated = self.sonar_deactiver

        
    def sonar_activer(self):
        self.temps_actif = self.echo.active_time
        self.compteur_distance = time.perf_counter()
    


    def sonar_deactiver(self):
        
        self.temps_inactif = self.echo.inactive_time
        
        distance = ( ( time.perf_counter() - self.temps_inactif - self.compteur_distance + self.temps_actif ) * VITESSE_SON / 2 ) * CONVERSION_CM
        self.distance_courante = calculer_moyenne_mobile(distance , self.tableau_distance)
        

    def envoyer_ondes(self):
        
        while(not self.arreter):    
            time.sleep(0.1)
            self.trigger.on()
            time.sleep(TEMPS_TRIGGER_ACTIF)
            self.trigger.off()
