#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022

import gpiozero
import numpy as np
import cv2
from robot import Robot


# Constantes
# Touches de clavier
W = 'w'
Q = 'q'
E = 'e'
A = 'a'
S = 's'
D = 'd'
SPACE = 'space'
PLUS = '+'
MOINS = '-'
X = 'x'

    
quitter = False

#Objet Robot
robot = Robot()

img = np.zeros((512,512,3),np.uint8)
cv2.imshow('Labo_1',img)

while (quitter):
    key = cv2.waitKey(100) # 100 milliseconds
    print("Allo")
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
        quitter = True
        robot.Arreter()

print("Au revoir!")
        

