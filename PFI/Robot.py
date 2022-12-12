#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 10 novembre 2022
import threading
from time import sleep
from State import State
from moteurs import Moteurs
from Direction import Direction
import math
import time

class Robot :
    def __init__(self, navigation , radioNavigation, lidar, en_marche):
        self.compteurAngle = 0
        self.moteurs = Moteurs()
        self.navigation = navigation
        self.radioNavigation = radioNavigation
        self.lidar = lidar
        self.x = 0
        self.y = 0
        self.en_marche = en_marche
        self.doit_avancer = False
        self.distanceAParcourir = 0
        self.distanceParcourue = 0
        self.axe = None
        self.arriver_position = True
        self.thread_avancer = None
        self.thread_Calculer_Distance_Parcourue = None
        self.angle = 0
        self.next_angle = 0
        self.obstacleDetecter = False
    def initialiserPosition(self):
        if(self.navigation.état == State.Immobile):
            self.x = self.radioNavigation.x
            self.y = self.radioNavigation.y
    def Start_Thread_Avancer(self, prochainX, prochainY):
        self.thread_avancer = threading.Thread(target = self.AvancerToPosition , args=(prochainX, prochainY))
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
            self.distanceParcourue = self.CalculerDistance(self.radioNavigation.x, self.x, self.radioNavigation.y, self.y)
            
    def CalculerDistance(self, x2, x1, y2, y1):
        x = x2 - x1
        y = y2 - y1
        return math.sqrt( pow(x, 2) + pow(y, 2))
    
    def CalculerAngle(self, x2, x1, y2, y1):
        deltaY = y2 - y1
        deltaX = x2 - x1
        return round(math.degrees(math.atan2(deltaY, deltaX)))
    
    def CorrectionAngle(self, prochainX, prochainY):
        print("correction")
        est_corriger = False
        angle = self.CalculerAngle(prochainX, self.x, prochainY, self.y)
        next_angle = self.navigation.angleX + angle
        if(angle > 2):
            self.Tourner(angle)
        while(not est_corriger):
            if(self.navigation.angleX == next_angle):
                self.Freiner()
                est_corriger = True
        
    def Avancer(self):
        self.navigation.état = State.Translation
        self.moteurs.avancer()
    def AvancerToPosition(self, prochainX, prochainY):
        
        self.y = self.radioNavigation.y
        self.x = self.radioNavigation.x
        self.distanceAParcourir = self.CalculerDistance(prochainX, self.x, prochainY, self.y)
        self.Avancer()
        self.compteurAngle = time.perf_counter()
        print("distance a parcourir ")
        print(self.distanceAParcourir)
        print("compteur")
        print(self.compteurAngle)
        while(self.distanceAParcourir > self.distanceParcourue):
            sleep(0.1)
            print("distance Parcourue")
            print(self.distanceParcourue)
            if(time.perf_counter() - self.compteurAngle > 1.5):
                self.CorrectionAngle(prochainX, prochainY)
                self.compteurAngle = 0
            self.navigation.état = State.Translation

        self.Freiner()
        self.arriver_position = True
            
        
    def VerifierDistanceLidar(self):
        distance = self.lidar.GetDistance(150)
        if(distance != None):
            return distance <= 0.2
    
    def PauseObstacle(self):
        self.Freiner()
        self.initialiserPosition()
        
    def Reculer(self):
        self.navigation.état = State.Translation
        self.moteurs.reculer()
            
    def Tourner(self, angle):
        if(angle > 0):
            self.moteurs.tourner(Direction.Gauche)
        else:
            self.moteurs.tourner(Direction.Droite)
        self.navigation.état = State.Rotation

    def Arreter(self):
        self.moteurs.arreter()
        self.navigation.état = State.Immobile
        
    def Freiner(self):
        self.moteurs.freiner()
        self.navigation.état = State.Immobile
    