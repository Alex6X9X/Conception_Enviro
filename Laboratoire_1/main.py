#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022

import gpiozero
from robot import Robot
from Attendre_Touche import Attendre_Touche

#Objet Robot
robot = Robot()

    
quitter = False


while (not quitter):
    Attendre_Touche(robot, quitter)

print("Au revoir!")
        

