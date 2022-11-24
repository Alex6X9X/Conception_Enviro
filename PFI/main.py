#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
arreter = False

imu = ICM20948()

navigation = Navigation(imu)
radioNavigation = RadioNavigation()
radioNavigation.demarrerCommunication()
robot = Robot(navigation , radioNavigation)




while not arreter:
    ##radioNavigation.getPosition()

    robot.Avancer()
    robot.Freiner()
    robot.Reculer()
    robot.Arreter()
    
navigation.en_marche = False
radioNavigation.en_marche = False
navigation.thread_calcul_position.join()
navigation.thread_affichage.join()
