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
        self.echo_gauche.when_activated = self.sonar_activer_g
        self.echo_droite.when_activated = self.sonar_activer_d
        self.echo_gauche.when_deactivated = self.sonar_deactiver_g
        self.echo_droite.when_deactivated = self.sonar_deactiver_d
        
    def sonar_activer_g(self):

        self.compteur_distanceg = time.perf_counter()
    
    def sonar_activer_d(self):

        self.compteur_distanced = time.perf_counter()

    def sonar_deactiver_g(self):
        ##calculer le temps avec compteur_distanceg et d

        distance  = (time.perf_counter() - self.compteur_distanceg) * VITESSE_SON /2
        #print(distance)
        self.distance_courante_gauche = self.calculer_moyenne_mobile(distance , self.tableau_distanceg)
        
        #print(self.distance_courante_gauche)
        #self.afficher_distances(self.distance_courante_gauche, 'gauche')
        
    def sonar_deactiver_d(self):
        distance = (time.perf_counter() - self.compteur_distanced) * VITESSE_SON / 2
        #print(distance)
        self.distance_courante_droite = self.calculer_moyenne_mobile(distance , self.tableau_distanced) 
        
        #print(self.distance_courante_droite) 
        #self.afficher_distances(self.distance_courante_droite, 'droite')

    def activer_sonar(self):
        while(not self.arreter):
            if(time.perf_counter() - self.compteur_trigger >= 0.1):
                self.compteur_trigger = time.perf_counter() 
                self.trigger_gauche.on()
                self.trigger_droite.on()
                time.sleep(TEMPS_TRIGGER_ACTIF)
                self.trigger_gauche.off()
                self.trigger_droite.off()
        print("Fini!")        
        self.Arreter()

    def calculer_moyenne_mobile(self , nouvelle_distance , tableau_distance):
        tableau_distance.append(nouvelle_distance)
        
        print(len(tableau_distance))
        if len(tableau_distance) >= FENETRE:
            print("-------------------------")
            temp_tab = self.copier_tableau(tableau_distance)
            temp_min = min(temp_tab)
            temp_max = max(temp_tab) 
            temp_tab.remove(temp_min)
            temp_tab.remove(temp_max)
            del tableau_distance[0]
            return sum(temp_tab)/len(temp_tab)
        
        return None
    
    def afficher_distances(self, distance, dir):
        img = np.zeros((512,512,3),np.uint8)
        cv2.imshow('Labo 2',img)
        
        org = (0,0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)
        line_type = 2
        
        print("Allo")
        if(distance != None):
            cv2.putText(img, 
                        "Sonar " + dir + " : " + str(round(distance)) + " cm", 
                        org, 
                        font, 
                        font_scale, 
                        font_color, 
                        line_type)    
        elif(distance== None):
            cv2.putText(img, 
                        "Sonar " + dir + " : Aucune données", 
                        org, 
                        font, 
                        font_scale, 
                        font_color, 
                        line_type)
            
    def copier_tableau(self, tab):
        tableau_copier = [len(tab)]
        
        for i in range(0, len(tab)):
            tableau_copier[i] = tab[i]
            
        return tableau_copier
