#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 27 octobre 2022

import cv2
import numpy as np
from Robot import Robot
from Navigation import Navigation
from Attendre_Touche import Attendre_Touche
from Console import Console
from icm20948 import ICM20948

arreter = False
robot = Robot()
imu = ICM20948()
navigation = Navigation(imu)


while not arreter:
    Attendre_Touche(robot , navigation)
    choix = cv2.waitKey(16)
    if  choix == ord('q'):
        arreter = True  
