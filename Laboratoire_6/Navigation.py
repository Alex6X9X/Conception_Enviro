import threading
from time import sleep


class Navigation : 
    
    def __init__(self):
        self.état = "immobile"
        self.thread_calcul_position = threading.Thread(target = self.Clignoter , args=())
        self.en_marche = True
    def _calculer_position(self):
        while(self.en_marche):
            sleep(0.05)
            if(self.état == "immobile"):
                ##À l’arrêt: le fil calcule les biais de gx et de ay en utilisant une moyenne fenêtrée. 
                pass
            elif(self.état == "rotation"):
                ##En rotation: le fil calcule la nouvelle orientation du robot en tenant compte du temps écoulé entre deux mesures et le biais calculé pour gx. 
                pass
            elif(self.état == "translation"):
                ##En translation: le fil calcule la nouvelle position en y du robot en tenant compte du temps écoulé entre deux mesures et le biais calculé pour ay. 
                pass

