#Alexandre Carle et Louis-philippe Rousseau
#15 septembre 2022
#Dernier changement le 19 septembre 2022

from time import sleep
from robot import Robot
from Odomètre import Odomètre

PORT_DEL_JAUNE = 10
PORT_DEL_VERTE = 9
SGT = 8   #Sonar Gauche Trigger...
SDT = 21  
SGE = 25  #Sonar Gauche Echo...
SDE = 20

arreter = False

robot = Robot()
odomètre = Odomètre(27,22)



while (not arreter):
    sleep(0.1)
    odomètre.avancer_distance(100)
    robot.Avancer()
    odomètre.attendre()
    robot.Arreter()
    arreter = True
   
