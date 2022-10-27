#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 27 octobre 2022

import cv2
import numpy as np
from moteurs import Moteurs
from icm20948 import ICM20948
arreter = False


imu = ICM20948()

while not arreter:

    choix = cv2.waitKey(16)
    if  choix == ord('q'):
        arreter = True  
