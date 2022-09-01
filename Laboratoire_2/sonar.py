#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

from array import array
import threading
import gpiozero
import time 
import numpy as np
import cv2

FENETRE = 10
TEMPS_TRIGGER_ACTIF = 0.000001
VITESSE_SON = 343

class Sonar:
    
    def __init__(self , port_triggerg , port_triggerd , port_echog , port_echod, arreter):
        self.compteur_trigger = time.perf_counter()
        self.thread = threading.Thread(target = self.activer_sonar , args=())
        self.compteur_distanceg = 0
        self.compteur_distanced = 0
        self.tableau_distanceg = []
        self.tableau_distanced = []
        self.trigger_gauche = gpiozero.DigitalOutputDevice(port_triggerg)
        self.trigger_droite = gpiozero.DigitalOutputDevice(port_triggerd)
        self.echo_gauche = gpiozero.DigitalInputDevice(port_echog)
        self.echo_droite = gpiozero.DigitalInputDevice(port_echod)
        self.arreter = arreter

        self.distance_courante_gauche = 0
        self.distance_courante_droite = 0
        
        self.initialiser_callbacks()
        
    def Demarrer(self):
        self.thread.start()
        
    def Arreter(self):
        self.thread.join()

        
    def initialiser_callbacks(self):
        ##when_activated / when_deactivated
        self.echo_gauche.when_activated = self.sonar_activer('g')
        self.echo_droite.when_activated = self.sonar_activer('d')
        self.echo_gauche.when_deactivated = self.sonar_deactiver('g')
        self.echo_droite.when_deactivated = self.sonar_deactiver('d')
        
    def sonar_activer(self, echo):
        print("Activé!")
        if(echo == 'g'):
            self.compteur_distanceg = time.perf_counter()
        elif(echo == 'd'):
            self.compteur_distanced = time.perf_counter()

    def sonar_deactiver(self , echo):
        ##calculer le temps avec compteur_distanceg et d
        print("DéActivé!")
        if(echo == 'g'):
            distance  = time.perf_counter() - self.compteur_distanceg * VITESSE_SON /2
            self.distance_courante_gauche = self.calculer_moyenne_mobile(distance , self.tableau_distanceg)
        if(echo == 'd'):  
            distance = time.perf_counter() - self.compteur_distanced * VITESSE_SON / 2
            self.distance_courante_droite = self.calculer_moyenne_mobile(distance , self.tableau_distanced)   
        
        self.Afficher_Distances()

    def activer_sonar(self):
        while(not self.arreter):
            if(time.perf_counter() - self.compteur_trigger >= 0.1):
                self.compteur_trigger = time.perf_counter() 
                self.trigger_gauche.on()
                self.trigger_droite.on()
                time.sleep(TEMPS_TRIGGER_ACTIF)
                self.trigger_gauche.off()
                self.trigger_droite.off()
                
        self.Arreter()

    def calculer_moyenne_mobile(self , nouvelle_distance , tableau_distance):
        tableau_distance.append(nouvelle_distance)
        
        if len(tableau_distance)>FENETRE:
            del tableau_distance[0]
            temp_tab = tableau_distance
            temp_min = min(temp_tab)
            temp_max = max(temp_tab) 
            temp_tab.remove(temp_min)
            temp_tab.remove(temp_max)
            return sum(temp_tab)/len(temp_tab)
        
        return None
    
    def Afficher_Distances(self, distance_gauche, distance_droite):
        img = np.zeros((512,512,3),np.uint8)
        cv2.imshow('Labo 2',img)
        
        #Rendre les strings plus simples
        if(distance_gauche != None and distance_droite == None):
            cv2.putText(img, "Sonar Gauche: " + str(distance_gauche) + " cm"  + " | Sonar Droite: Aucune données")    
        elif(distance_gauche == None and distance_droite != None):
            cv2.putText(img, "Sonar Gauche: Aucune données | Sonar Droite:" + str(distance_droite) + " cm")
        elif(distance_droite != None and distance_gauche != None):    
            cv2.putText(img, "Sonar Gauche: " + str(distance_gauche) + "cm" + " | " + "Sonar Droite:" + str(distance_droite) + " cm")
        else:
            cv2.putText(img, "Sonar Gauche: Aucune données | Sonar Droite: Aucune données")   
