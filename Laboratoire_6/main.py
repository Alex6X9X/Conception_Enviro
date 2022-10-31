#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 27 octobre 2022

import cv2
import numpy as np
from Robot import Robot
from Navigation import Navigation
from Attendre_Touche import Attendre_Touche
from Console import Console
from icm20948 import ICM20948
angleXFile = open('angleX.txt' , 'wt')
vyFile = open('vy.txt' , 'wt')
arreter = False
robot = Robot()
imu = ICM20948()
navigation = Navigation(imu , robot ,ayFile,PosYFile,angleXFile,vyFile )




while not arreter:
    arreter = Attendre_Touche(robot , navigation)
navigation.en_marche = False
navigation.thread_calcul_position.join()