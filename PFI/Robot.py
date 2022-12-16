#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 10 novembre 2022
import threading
from time import sleep
from State import State
from moteurs import Moteurs
from Direction import Direction
import math
import time

DELTA_ANGLE = 2
DISTANCE_MIN_LIDAR = 0.2

class Robot :
    def __init__(self, navigation , radioNavigation, lidar, en_marche):
        #self.compteurAngle = 0
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
        self.arriver_position = False
        self.thread_avancer = None
        self.thread_Calculer_Distance_Parcourue = None
        self.angle = 0
        self.angleX = 0
        self.next_angle = 0
        self.obstacleDetecter = False
        self.avance = True
        self.IsStopped = False
        
    def initialiserPosition(self):
        #while(self.radioNavigation.x == 0 and self.radioNavigation.y == 0):
        #    print("Initializing...")
        self.x = self.radioNavigation.x
        self.y = self.radioNavigation.y
                
    def Start_Thread_Avancer(self, prochainX, prochainY, angle_depart):
        self.avance = True
        self.arriver_position = False
        self.thread_avancer = threading.Thread(target = self.AvancerToPosition , args=(prochainX, prochainY, angle_depart))
        self.thread_Calculer_Distance_Parcourue = threading.Thread(target = self.CalculerDistanceParcourue , args=(prochainX, prochainY))     
        self.thread_avancer.start()
        self.thread_Calculer_Distance_Parcourue.start()

        
    def Stop_Thread_Avancer(self):
        self.thread_avancer.join()
        self.thread_Calculer_Distance_Parcourue.join()
        
    def CalculerDistanceParcourue(self, prochainX, prochainY):
        while(self.avance):
            sleep(0.1)
            self.distanceParcourue = self.CalculerDistance(prochainX, self.radioNavigation.x, prochainY, self.radioNavigation.y)
            print("distance parcourue" ,self.distanceParcourue)
    def CalculerDistance(self, x2, x1, y2, y1):
        x = x2 - x1
        y = y2 - y1
        res = pow(y, 2) + pow(x, 2)
        return math.sqrt(res)
    
    def CalculerAngle(self, x2, x1, y2, y1):
        deltaY = y2 - y1
        deltaX = x2 - x1
        return round(math.degrees(math.atan2(deltaY, deltaX)))
    
    def CorrectionAngle(self, angle):
        print("correction")
        est_corriger = False
        #angle = self.CalculerAngle(prochainX, self.x, prochainY, self.y)
        #next_angle = self.navigation.angleX + angle
        #print(angle)
        if(angle > DELTA_ANGLE):
            self.Tourner(angle)
        while(not est_corriger):
            if(self.navigation.angleX == angle):
                self.Freiner()
                est_corriger = True
        
    def Avancer(self):
        self.navigation.état = State.Translation
        self.moteurs.avancer()
    def AvancerToPosition(self, prochainX, prochainY, angle_depart):
        self.distanceAParcourir = self.CalculerDistance(prochainX, self.radioNavigation.x, prochainY, self.radioNavigation.y)
        stop_range = self.distanceAParcourir * 0.55
        #self.compteurAngle = time.perf_counter()
        print("distance a parcourir ")
        print(self.distanceAParcourir)
        #print("compteur")
        #print(self.compteurAngle)
        while(self.avance):
            sleep(0.01)
            
            while(self.VerifierDistanceLidar()):
                print('Jarrete')
                self.PauseObstacle()
                #if(not self.IsStopped):
                    #print('Jarrete')
                    #self.PauseObstacle()
                    #self.IsStopped = True
            self.Avancer()

            if(stop_range > self.distanceParcourue and self.distanceParcourue != 0):
                self.avance = False

                
            #angle = self.CalculerAngle(prochainX, self.x, prochainY, self.y)
            #if(time.perf_counter() - self.compteurAngle > 1.5):
            #if(angle != angle_depart):
                #self.CorrectionAngle(angle)
                #self.compteurAngle = 0

        self.Freiner()
        self.arriver_position = True
            
        
    def VerifierDistanceLidar(self):
        distance = self.lidar.GetDistance()
        print("distance" , distance)
        if(distance != None and distance != []):
            if(isinstance(distance , int)):
                 return distance < 800
            else:
                return min(distance) < 800

        
    
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
    