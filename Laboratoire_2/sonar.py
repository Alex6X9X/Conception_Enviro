from ast import Pass
import threading
import gpiozero
import time 
FENETRE = 10
TEMPS_TRIGGER_ACTIF = 0.000001
class Sonar:
    
    def __init__(self , port_triggerg , port_triggerd , port_echog , port_echod):
        self.compteur_trigger = time.perf_counter()
        self.temps_courant_trigger = 0
        self.thread = threading.Thread(target = self.activer_sonar , args=())
        self.compteur_distanceg = 0
        self.compteur_distanced = 0
        self.tableau_distanceg = []
        self.tableau_distanced = []
        self.trigger_gauche = gpiozero.DigitalOutputDevice(port_triggerg)
        self.trigger_droite = gpiozero.DigitalOutputDevice(port_triggerd)
        self.echo_gauche = gpiozero.DigitalInputDevice(port_echog)
        self.echo_droite = gpiozero.DigitalInputDevice(port_echod)

        self.distance_courante_gauche = 0
        self.distance_courante_droite = 0

        
    def initialiser_callbacks(self):
        ##when_activated / when_deactivated
        self.echo_gauche.when_activated = self.sonar_activer('g')
        self.echo_droite.when_activated = self.sonar_activer('d')
        self.echo_gauche.when_deactivated = self.sonar_deactiver('g')
        self.echo_droite.when_deactivated = self.sonar_deactiver('d')
        
    def sonar_activer(self,echo):
        if(echo == 'g'):
            self.compteur_distanceg = time.perf_counter()
        elif(echo == 'd'):
            self.compteur_distanced = time.perf_counter()

    def sonar_deactiver(self , echo):
        ##calculer le temps avec compteur_distanceg et d
        if(echo == 'g'):
            distance  = self.compteur_distanceg * 343 /2
            self.distance_courante_gauche = self.calculer_moyenne_mobile(distance , self.tableau_distanceg)
        if(echo == 'd'):
            distance = self.compteur_distanced * 343 / 2
            self.distance_courante_droite = self.calculer_moyenne_mobile(distance , self.tableau_distanced)   

    def activer_sonar(self):
        while(self.arreter):
            if(self.compteur_trigger - self.temps_courant_trigger >= 0.1):
                self.temps_courant_trigger = self.compteur_trigger
                self.trigger_gauche.on()
                self.trigger_droite.on()
                time.sleep(TEMPS_TRIGGER_ACTIF)
                self.trigger_gauche.off()
                self.trigger_droite.off()

    def calculer_moyenne_mobile(self , nouvelle_distance , tableau_distance):
        tableau_distance.append(nouvelle_distance)
        
        
        if len(tableau_distance)>FENETRE:
            del tableau_distance[0]
            temp_tab = tableau_distance
            del min(temp_tab)
            del max(temp_tab)
            return sum(temp_tab)/len(temp_tab)
        
        return None
