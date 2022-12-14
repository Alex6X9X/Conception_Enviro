#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from time import sleep
from Robot import Robot
from Navigation import Navigation
from RadioNavigation import RadioNavigation
from Lidar import Lidar
from State import State
from Direction import Direction

TEMPS_CALIBRATION = 5
en_marche = True



radioNavigation = RadioNavigation(en_marche)



beggining_of_circuit = True

sleep(TEMPS_CALIBRATION)

##tabPosition = [(6 , -0.34), (7.94 , 0.27) , (8.15 , 2.63) , (6.2 , 2.78)]
tabPosition = [(12.76 , 5.73)]
has_started = False

sleep(10)
radioNavigation.thread_get_position.join()
radioNavigation.fermerConnection()
      
    #print("x" , radioNavigation.x)
    #print("y", radioNavigation.y)

        
    

    

#navigation.thread_affichage.join()
