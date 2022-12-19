#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from time import sleep
from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
from Lidar import Lidar
from State import State
from Direction import Direction


en_marche = True

imu = ICM20948()
angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
lidar = Lidar(en_marche)
lidar.thread_scan_lidar.start()
robot = Robot(navigation , radioNavigation, lidar, en_marche)
has_started_turning = False

tabPosition = [(6 , 0.60) , (8.20 , 0.9), (8.20, 2.20), (6.40, 2.25)]
index = 0
has_started = False
sleep(5)
robot.initialiserPosition()
while(en_marche):
    
    if(not has_started):
        robot.Start_Thread_Avancer(tabPosition[index][0], tabPosition[index][1])
        has_started = True

    if(robot.arriver_position):
        if(not has_started_turning):
            robot.Stop_Thread_Avancer()
            robot.Tourner(Direction.Gauche)
            index += 1
            has_started_turning = True
            
        ##Entrer dans cette condition quand l'angle du robot à atteint 90 degrées
        #Nous avons mis 85 degrées pour compenser les délais matériels (Si == 90, il tournait trop)
        if(navigation.angleX >= robot.angleX + 85 or navigation.angleX <= robot.angleX - 85 and has_started_turning):
            robot.Freiner()
            robot.angleX = navigation.angleX
            has_started = False
            has_started_turning = False
            
    if(index == len(tabPosition)):
        en_marche = False
        robot.Freiner()
        
radioNavigation.en_marche = False
lidar.en_marche = False
navigation.en_marche = False
radioNavigation.thread_get_position.join()
lidar.thread_scan_lidar.join()
navigation.thread_calcul_position.join()
