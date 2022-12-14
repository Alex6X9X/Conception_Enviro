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

TEMPS_CALIBRATION = 5
en_marche = True

imu = ICM20948()
angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
lidar = Lidar(en_marche)
lidar.thread_scan_lidar.start()
radioNavigation.thread_get_position.start()
robot = Robot(navigation , radioNavigation, lidar, en_marche)

beggining_of_circuit = True

sleep(TEMPS_CALIBRATION)

##tabPosition = [(6 , -0.34), (7.94 , 0.27) , (8.15 , 2.63) , (6.2 , 2.78)]
tabPosition = [(12.76 , 5.73)]
has_started = False
robot.initialiserPosition()
while en_marche:
    sleep(0.1)

    #print("x" , radioNavigation.x)
    #print("y", radioNavigation.y)

        
    
    
      
    

#navigation.thread_affichage.join()
