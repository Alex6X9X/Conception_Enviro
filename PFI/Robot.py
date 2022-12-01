#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 10 novembre 2022
import threading
from time import sleep
from State import State
from moteurs import Moteurs
class Robot :
    def __init__(self, navigation , radioNavigation, en_marche):
        self.moteurs = Moteurs()
        self.navigation = navigation
        self.radioNavigation = radioNavigation
        self.x = 0
        self.y = 0
        self.en_marche = en_marche
        self.doit_avancer = False
        self.has_started = False
        self.distanceAParcourir = 0
        self.distanceParcourue = 0
        self.axe = None
        self.arriver_position = False
        self.obstacle_in_the_way = False
    def initialiserPosition(self):
        if(self.navigation.état == State.Immobile):
            self.x = self.radioNavigation.x
            self.y = self.radioNavigation.y
    def CalculerDistance(self , positionToGoTo , xOuY):
        self.y = self.radioNavigation.y
        self.x = self.radioNavigation.x
        if(xOuY == 'Y'):
            print(abs(positionToGoTo - self.y))
            self.distanceAParcourir = abs(positionToGoTo - self.y)
            self.axe = 'Y'
        elif(xOuY == 'X'):
            self.distanceAParcourir = abs(positionToGoTo - self.x)
            self.axe = 'X'
    def Start_Thread_Avancer(self):
        self.thread_avancer = threading.Thread(target = self.AvancerToPosition , args=())
        self.thread_Calculer_Distance_Parcourue = threading.Thread(target = self.CalculerDistanceParcourue , args=())
        self.thread_avancer.start()
        self.thread_Calculer_Distance_Parcourue.start()
    def Stop_Thread_Avancer(self):
        self.thread_avancer.join()
        self.thread_Calculer_Distance_Parcourue.join()
    def CalculerDistanceParcourue(self):
        self.arriver_position = False
        while(self.en_marche):
            sleep(0.1)
            if(self.axe == 'Y'):
                self.distanceParcourue = abs(self.radioNavigation.y - self.y)
            elif(self.axe =='X'):
                self.distanceParcourue =  abs(self.radioNavigation.x - self.x)
           


    def Avancer(self):
        self.navigation.état = State.Translation
        self.moteurs.avancer()
    def AvancerToPosition(self):
        self.Avancer()
       
        while(self.distanceAParcourir < self.distanceParcourue):
            sleep(0.1)
            self.navigation.état = State.Translation

        self.Freiner()
        self.x = self.radioNavigation.x
        self.y = self.radioNavigation.y
        self.arriver_position = True
            
        
    def PauseObstacle(self):
        self.obstacle_in_the_way = True
        self.Freiner()
        self.initialiserPosition()
    def Reculer(self):
        self.navigation.état = State.Translation
        self.moteurs.reculer()
            
    def Tourner(self, dir):
        self.navigation.état = State.Rotation
        self.moteurs.tourner(dir)

    def Arreter(self):
        self.moteurs.arreter()
        self.navigation.état = State.Immobile
        
    def Freiner(self):
        self.moteurs.freiner()
        self.navigation.état = State.Immobile
    