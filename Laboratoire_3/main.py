#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 12 septembre 2022

from time import sleep
from robot import Robot
from Odomètre import Odomètre


import cv2

PORT_DEL_JAUNE = 10
PORT_DEL_VERTE = 9
SGT = 8   #Sonar Gauche Trigger...
SDT = 21  
SGE = 25  #Sonar Gauche Echo...
SDE = 20

arreter = False

robot = Robot()
odomètre = Odomètre(2,2)



print("Appuyer sur la touche 'x' pour quitter le programme...")

#Démarrage des threads


while (not arreter):
    odomètre.avancer_distance(100)
    robot.Avancer()
    odomètre.attendre()
    robot.Arreter()
   
