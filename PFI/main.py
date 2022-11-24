#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
from Lidar import Lidar
en_marche = True

imu = ICM20948()

navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation()
radioNavigation.demarrerCommunication()
robot = Robot(navigation , radioNavigation, en_marche)
#lidar = Lidar(en_marche)

#robot.Tourner(0)
#if(navigation.angleX < -90):
#    robot.Freiner()
    


while en_marche:
    radioNavigation.getPosition()
    print(radioNavigation.x)
    print(radioNavigation.y)
    #lidar.ScanLidar()
    #lidar.GetDistance(0)
    robot.Avancer()
    robot.Freiner()
    robot.Reculer()
    robot.Arreter()
    
navigation.en_marche = False
#radioNavigation.en_marche = False
navigation.thread_calcul_position.join()
navigation.thread_affichage.join()
