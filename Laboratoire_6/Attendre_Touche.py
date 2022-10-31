#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022
#Dernier changement le 28 août 2022

import numpy as np
import cv2
from State import State

# Constantes
# Touches de clavier
W = 'w'
Q = 'q'
E = 'e'
A = 'a'
S = 's'
D = 'd'
SPACE = ' '
PLUS = '+'
MOINS = '-'
X = 'x'


# Paramètre: Un objet de type Robot() pour le déplacement du véhicule
# Retourne un booléen
def Attendre_Touche(robot , navigation):
    
    img = np.zeros((512,512,3),np.uint8)
    cv2.imshow('Labo 6',img)
    
    key = cv2.waitKey(16) # 100 milliseconds
    
    if key == ord(W): 
        navigation.état = State.Translation
        robot.Avancer()
        
    elif key == ord(A):
        navigation.état = State.Rotation
        robot.Tourner('g')
    
    elif key == ord(S):
        navigation.état = State.Translation
        robot.Reculer()
    
    elif key == ord(D):
        navigation.état = State.Rotation
        robot.Tourner('d')
    
    elif key == ord(SPACE):
        navigation.état = State.Immobile
        robot.Freiner()
   
    elif key == ord(X):
        robot.Arreter()
        return True
    
    return False