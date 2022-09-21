#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 19 septembre 2022
import faulthandler;
faulthandler.enable()

from time import sleep
from robot import Robot
from Odomètre import Odomètre

arreter = False

robot = Robot()
odomètre = Odomètre()


while (not arreter):
    sleep(0.1)
    odomètre.avancer_distance(100)
    robot.Avancer()
    odomètre.attendre()
    robot.Arreter()
    arreter = True
   
