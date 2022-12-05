#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from time import sleep
from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
from Lidar import Lidar
from State import State
from Axe import Axe
from Direction import Direction

TEMPS_CALIBRATION = 4

en_marche = True

imu = ICM20948()
angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
radioNavigation.demarrerCommunication()
radioNavigation.thread_get_position.start()
robot = Robot(navigation , radioNavigation, en_marche)
robot.initialiserPosition()
#lidar = Lidar(en_marche)

sleep(TEMPS_CALIBRATION)

#robot.Tourner(Direction.Droite)
#if(navigation.angleX < -90):
#    robot.Freiner()
#tabVraiPosition = [(0, 0), (12.11, 0), (13.0, 7.54), (0.70, 8.66)]    
tabPosition = [0,7.80, 1.60, 6]
has_started = False

index = 0 
while en_marche:
    
    sleep(0.1)
   ## print("x")
    print(str(radioNavigation.x))
   ## print("y")
    print(str(radioNavigation.y))
   ## print("---")
    

    #lidar.ScanLidar()
    #lidar.GetDistance(150)
    #robot.Avancer()


    if(not has_started):
        robot.Start_Thread_Avancer()
        index += 1
        has_started = True
    if(robot.arriver_position):
        robot.Stop_Thread_Avancer()
        angle = robot.CalculerAngle(0, robot.x, 0, robot.y)
        next_angle = navigation.angleX + angle
        robot.Tourner(angle)
        robot.arriver_position = False

    if(navigation.état == State.Rotation):
        if(navigation.angleX == next_angle):
            robot.Freiner()
            has_started = False
        
    

        
    ##ici ajouter vérification du Lidar pour vérifier les obstacles et arrêter le robot si c'est le cas
    ##if(robot.obstacle_in_the_way):
      ##   robot.PauseObstacle()
        ## robot.Stop_Thread_Avancer()
       ##  robot.CalculerDistance(tabPosition[index] , tabAxes[index])

    

en_marche=False
#radioNavigation.en_marche = False
radioNavigation.fermerConnection()
navigation.thread_calcul_position.join()
#navigation.thread_affichage.join()
