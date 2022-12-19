#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

#Main avec la fonctionnalité du parcours amélioré non fonctionnel

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

beggining_of_circuit = True


tabPosition = [(6 , -0.34), (7.94 , 0.27) , (8.15 , 2.63) , (6.2 , 2.78)]
tabPosition = [(12.20 , 5.80) , (12.57 , 7.04)]
has_started = False
angle = 0
index = 0 
robot.initialiserPosition()
while en_marche:
    sleep(0.1)

    robot.obstacleDetecter = robot.VerifierDistanceLidar()
    if(robot.obstacleDetecter):
        robot.Freiner()
        robot.Stop_Thread_Avancer()
        has_started = False
    if(not has_started and not robot.obstacleDetecter):
        robot.Start_Thread_Avancer(tabPosition[index][0], tabPosition[index][1], angle)
        has_started = True
    if(robot.arriver_position):
        if(not beggining_of_circuit):
            index += 1
            robot.Stop_Thread_Avancer()
            beggining_of_circuit = True
        if(index == len(tabPosition)):
          en_marche = False

        else:
          previous_angle = navigation.angleX
          angle = robot.CalculerAngle(tabPosition[index][0], robot.x, tabPosition[index][1], robot.y)

          if(angle != previous_angle):
                robot.CorrectionAngle(angle)
          robot.arriver_position = False

    if(navigation.état == State.Rotation):
        if(navigation.angleX >= angle - 5 or navigation.angleX <= angle + 5):
            robot.Freiner()
            has_started = False
       
radioNavigation.en_marche = False
lidar.en_marche = False
navigation.en_marche = False
radioNavigation.thread_get_position.join()
navigation.thread_calcul_position.join()
lidar.thread_scan_lidar.join() 
    
