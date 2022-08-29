#Alexandre Carle et Louis-philippe Rousseau
#25 août 2022
#Dernier changement le 28 août 2022

import gpiozero
from robot import Robot
from Attendre_Touche import Attendre_Touche

#Objet Robot
robot = Robot()

    
quitter = False

print("Appuyer sur la touche 'x' pour quitter le programme...")

while (not quitter):
    quitter = Attendre_Touche(robot)

print("Au revoir!")
        

