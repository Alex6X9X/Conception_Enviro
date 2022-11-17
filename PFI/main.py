#Auteurs: Alexandre Carle et Louis-philippe Rousseau et Guillaume Légaré
#Dernier changement 14 novembre 2022

from Robot import Robot
from Navigation import Navigation
from Attendre_Touche import Attendre_Touche
from icm20948 import ICM20948
arreter = False
robot = Robot()
imu = ICM20948()
navigation = Navigation(imu , robot)




while not arreter:
    arreter = Attendre_Touche(robot , navigation)
navigation.en_marche = False
navigation.thread_calcul_position.join()
navigation.thread_affichage.join()