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

TEMPS_CALIBRATION = 4

en_marche = True

imu = ICM20948()
angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
lidar = Lidar(en_marche)
radioNavigation.demarrerCommunication()
radioNavigation.thread_get_position.start()
robot = Robot(navigation , radioNavigation, lidar, en_marche)
robot.initialiserPosition()

sleep(TEMPS_CALIBRATION)

#robot.Tourner(Direction.Droite)
#if(navigation.angleX < -90):
#    robot.Freiner()
#tabVraiPosition = [(0, 0), (12.11, 0), (13.0, 7.54), (0.70, 8.66)]    
tabPosition = [(0,7.80), 1.60, 6]
has_started = False

index = 0 
while en_marche:
    
    sleep(0.1)
   ## print("x")
    print(str(radioNavigation.x))
   ## print("y")
    print(str(radioNavigation.y))
   ## print("---")


    if(not has_started):
        robot.Start_Thread_Avancer(tabPosition[index][0], tabPosition[index][1])
        has_started = True
    if(robot.arriver_position):
        index += 1
        robot.Stop_Thread_Avancer()
        if(index == len(tabPosition)):
          en_marche = False
          #radioNavigation.en_marche = False
          radioNavigation.fermerConnection()
          navigation.thread_calcul_position.join()
          lidar.thread_scan_lidar.join()
        else:
          angle = robot.CalculerAngle(0, robot.x, 0, robot.y)
          next_angle = navigation.angleX + angle
          robot.Tourner(angle)
          robot.arriver_position = False

    if(navigation.état == State.Rotation):
        if(navigation.angleX == next_angle):
            robot.Freiner()
            has_started = False
        
    
    if(robot.VerifierDistanceLidar()):
        robot.PauseObstacle()
        robot.Stop_Thread_Avancer()
        has_started = False
      
    

#navigation.thread_affichage.join()
