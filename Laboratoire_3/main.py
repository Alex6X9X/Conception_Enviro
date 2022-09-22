#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 19 septembre 2022

import time
from robot import Robot
from Odomètre import Odomètre

robot = Robot()
odomètre = Odomètre()

odomètre.avancer_distance(100)
robot.Avancer()
odomètre.attendre()
robot.Freiner()
time.sleep(1)
   
