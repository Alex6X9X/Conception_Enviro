from ast import Pass
import threading
import gpiozero
FENETRE = 10
class Sonar:
    
    def __init__(self):
        self.thread = threading.Thread(target = self.activer_sonar , args=())
        self.sonar_activer = False
        self.sonar_deactiver = False
        self.compteur_distance = 0
        self.tableau_distance = []
        self.sonar_gauche = 0
        self.sonar_droite = 0
        
        
    def initialiser_callbacks(self):
        ##when_activated / when_deactivated

        pass
    def activer_sonar(self):
        pass
    def calculer_moyenne_mobile(self , nouvelle_distance):
        self.tableau_distance.append(nouvelle_distance)
        if len(self.tableau_distance)>FENETRE:
            del self.tableau_distance[0]
        return sum(self.tableau_distance)/len(self.tableau_distance)
