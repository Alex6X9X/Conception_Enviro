#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 10 novembre 2022

import numpy as np
import cv2
from State import State



# Paramètre: Un objet de type Robot() pour le déplacement du véhicule
# Retourne un booléen
def Attendre_Touche(robot , navigation):
    
    img = np.zeros((512,512,3),np.uint8)
    cv2.imshow('Labo 6',img)
    
    key = cv2.waitKey(16)
    
    if key == ord('w'): 
        navigation.état = State.Translation
        robot.Avancer()
        
    elif key == ord('a'):
        navigation.état = State.Rotation
        robot.Tourner('g')
    
    elif key == ord('s'):
        navigation.état = State.Translation
        robot.Reculer()
    
    elif key == ord('d'):
        navigation.état = State.Rotation
        robot.Tourner('d')
    
    elif key == ord(' '):
        navigation.état = State.Immobile
        robot.Freiner()
   
    elif key == ord('x'):
        robot.Arreter()
        return True
    
    return False