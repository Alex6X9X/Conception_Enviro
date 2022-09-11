#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

import threading
from Console import Console
import gpiozero
import time 
import numpy as np
import cv2

FENETRE = 10
TEMPS_TRIGGER_ACTIF = 0.000001
VITESSE_SON = 343

class Sonar:
    
    def __init__(self , port_triggerg , port_triggerd , port_echog , port_echod, arreter):
        
        #Sonars
        self.trigger_gauche = gpiozero.DigitalOutputDevice(port_triggerg)
        self.trigger_droite = gpiozero.DigitalOutputDevice(port_triggerd)
        self.echo_gauche = gpiozero.DigitalInputDevice(port_echog)
        self.echo_droite = gpiozero.DigitalInputDevice(port_echod)
        self.compteur_trigger = time.perf_counter()
        self.temps_inactif = 0
        self.temps_actif = 0
        
        self.thread = threading.Thread(target = self.activer_sonar , args=())
        
        #Distances
        self.compteur_distanceg = 0
        self.compteur_distanced = 0
        self.distance_courante_gauche = 0
        self.distance_courante_droite = 0
        self.tableau_distanceg = []
        self.tableau_distanced = []
        
        #Booléen pour l'arrêt du programme
        self.arreter = arreter

        self.console = Console()
        
        self.initialiser_callbacks()
        
    def Demarrer(self):
        self.thread.start()
        
    def Arreter(self):
        self.thread.join()

    def initialiser_callbacks(self):
        self.echo_gauche.when_activated = self.sonar_activer_g
        self.echo_droite.when_activated = self.sonar_activer_d
        self.echo_gauche.when_deactivated = self.sonar_deactiver_g
        self.echo_droite.when_deactivated = self.sonar_deactiver_d
        
    def sonar_activer_g(self):
        
        #print('active gauche ' + str(self.echo_gauche.active_time))
        self.temps_actif = self.echo_gauche.active_time
        self.compteur_distanceg = time.perf_counter()
    
    def sonar_activer_d(self):
        #print('active gauche ' + str(self.echo_droite.active_time))
        self.temps_actif = self.echo_droite.active_time
        self.compteur_distanced = time.perf_counter()

    def sonar_deactiver_g(self):
        
        self.temps_inactif = self.echo_gauche.inactive_time
        
        distance = (time.perf_counter() - self.compteur_distanceg - (self.temps_inactif + self.temps_actif)) * VITESSE_SON /2

        self.distance_courante_gauche = self.calculer_moyenne_mobile(distance , self.tableau_distanceg)
        
        print("Gauche: " + str(self.distance_courante_gauche))
        #self.console.afficher_distances(self.distance_courante_gauche, 'gauche')
        
    def sonar_deactiver_d(self):

        self.temps_inactif = self.echo_droite.inactive_time
        
        distance = (time.perf_counter() - self.compteur_distanced - (self.temps_inactif + self.temps_actif)) * VITESSE_SON / 2

        self.distance_courante_droite = self.calculer_moyenne_mobile(distance , self.tableau_distanced) 
        
        print("Droite: " + str(self.distance_courante_droite))
        #self.console.afficher_distances(self.distance_courante_droite, 'droite')

    def activer_sonar(self):
        self.console.afficher()
        
        while(not self.arreter):
            if(time.perf_counter() - self.compteur_trigger >= 0.1):
                self.compteur_trigger = time.perf_counter() 
                self.trigger_gauche.on()
                self.trigger_droite.on()
                time.sleep(TEMPS_TRIGGER_ACTIF)
                self.trigger_gauche.off()
                self.trigger_droite.off() 

    def calculer_moyenne_mobile(self , nouvelle_distance , tableau_distance):
        tableau_distance.append(nouvelle_distance)
        
        if len(tableau_distance) >= FENETRE:
            temp_tab = self.copier_tableau(tableau_distance)
            temp_min = min(temp_tab)
            temp_max = max(temp_tab) 
            temp_tab.remove(temp_min)
            temp_tab.remove(temp_max)
            del tableau_distance[0]
            return sum(temp_tab)/len(temp_tab)
        
        return None
            
    def copier_tableau(self, tab):
        return tab.copy()