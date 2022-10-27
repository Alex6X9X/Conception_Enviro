#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 27 octobre 2022

import cv2
import numpy as np
from moteurs import Moteurs
arreter = False


while not arreter:

    choix = cv2.waitKey(16)
    if  choix == ord('q'):
        arreter = True  
