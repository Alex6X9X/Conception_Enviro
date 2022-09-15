#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022
#Dernier changement le 28 août 2022

import numpy as np
import cv2

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
def Attendre_Touche(robot):
    
    #img = np.zeros((512,512,3),np.uint8)
    #cv2.imshow('Labo 1',img)
    
    key = cv2.waitKey(100) # 100 milliseconds
    
    if key == ord(W): 
        robot.Avancer()

    elif key == ord(Q):
        robot.Avancer('g')
        
    elif key == ord(E):
        robot.Avancer('d')
        
    elif key == ord(A):
        robot.Tourner_90('g')
    
    elif key == ord(S):
        robot.Reculer()
    
    elif key == ord(D):
        robot.Tourner_90('d')
    
    elif key == ord(SPACE):
        robot.Arreter()
        
    elif key == ord(PLUS):
        robot.Augmenter_Vitesse()
        
    elif key == ord(MOINS):
        robot.Diminuer_Vitesse()
        
    elif key == ord(X):
        robot.Arreter()
        return True
    
    return False