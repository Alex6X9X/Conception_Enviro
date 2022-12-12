#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from time import sleep
from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
from Lidar import Lidar
from State import State
from Direction import Direction

TEMPS_CALIBRATION = 4

en_marche = True

imu = ICM20948()
angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)

radioNavigation.demarrerCommunication()
radioNavigation.thread_get_position.start()


has_started = True
sleep(TEMPS_CALIBRATION)

index = 0 
while en_marche:
    
    sleep(0.1)
   ## print("x")
    print(str(radioNavigation.x))
   ## print("y")
    print(str(radioNavigation.y))
   ## print("---")

    
        