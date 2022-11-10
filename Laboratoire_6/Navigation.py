import threading
import time
from time import sleep
from icm20948 import ICM20948
from calculer_moyenne_mobile import calculer_moyenne_mobile
from State import State
import csv

G = 9.80665 #m/s2
TOUR_COMPLET = 360 #Degrés

class Navigation : 
    
    def __init__(self , imu , robot):
        
        self.état = 0
        self.thread_calcul_position = threading.Thread(target = self._calculer_position , args=())
        self.en_marche = True
        self.ax= None 
        self.ay= None 
        self.az= None
        self.gx= None
        self.gy= None
        self.gz= None
        self.imu = imu
        self.robot = robot
        self.thread_calcul_position.start()
        self._tab_biais_gx = []
        self._tab_biais_ay = []
        self._biais_gx = 0
        self._biais_ay = 0
        self.compteur = 0
        self.deltaTime = 0
        self.ancien_compteur = 0
        self.angleX = 0
        self.gx_precedent = 0
        self.ay_precedent = 0
        self.vy = 0
        self.vy_precedent = 0
        self.posY = 0
        
    def _calculer_position(self):
        while(self.en_marche):
            sleep(0.05)
            self._get_gyro_data()
            
            if(self.état == State.Immobile):
                self._biais_gx = calculer_moyenne_mobile(self.gx , self._tab_biais_gx)
                self._biais_ay = calculer_moyenne_mobile(self.ay , self._tab_biais_ay)
                self.vy = 0
                self.vy_precedent = 0
                print("Biais ay:" + str(self._biais_ay))
                ##if(self._biais_ay != None):
                  ##  print(self.ay - self._biais_ay)
                
               
                
            elif(self.état ==  State.Rotation):
                self.gx = self.gx - self._biais_gx
                self.angleX += self.deltaTime * (self.gx + self.gx_precedent) / 2
                self.gx_precedent = self.gx
                
                #angleXFile = open('angleX.txt' , 'wt')
                #angleXFile.write(str(self.angleX))
                #angleXFile.close()
                    
                print("Angle X:" + str(self.angleX))

                
            elif(self.état ==  State.Translation):
                self.ay = self.ay - self._biais_ay
                self.vy += self.deltaTime * (self.ay + self.ay_precedent) / 2 * G 
                self.posY += self.deltaTime * (self.vy + self.vy_precedent) / 2 
                self.ay_precedent = self.ay
                self.vy_precedent = self.vy

                #ayFile = open('ay.txt', 'wt')
                #PosYFile = open('posY.txt' , 'wt')
                #vyFile = open('vy.txt' , 'wt')
                #ayFile.write(str(self.ay))
                #PosYFile.write(str(self.posY))
                #vyFile.write(str(self.vy))

                #ayFile.close()
                #PosYFile.close()
                #vyFile.close()
                
                #print("Accélération:" + str(self.ay))
                print("Position Y: " + str(self.posY))
                #print("Vitesse:" + str(self.vy))
               
                

    def _get_gyro_data(self):
        self.ax, self.ay, self.az, self.gx, self.gy, self.gz = self.imu.read_accelerometer_gyro_data()
        self.ancien_compteur = self.compteur
        self.compteur = time.perf_counter()
        self.deltaTime = self.compteur - self.ancien_compteur
