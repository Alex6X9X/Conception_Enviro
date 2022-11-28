#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from time import sleep
from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
from Lidar import Lidar
from State import State
en_marche = True

imu = ICM20948()
current_angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
radioNavigation.demarrerCommunication()
radioNavigation.thread_get_position.start()
robot = Robot(navigation , radioNavigation, en_marche)
robot.initialiserPosition()
current_angle = navigation.angleX
#lidar = Lidar(en_marche)

#robot.Tourner(0)
#if(navigation.angleX < -90):
#    robot.Freiner()
    
tabPosition = [0,7.80, 1.60, 6]
tabAxes = ['Y' , 'X' , 'Y' , 'X']

index = 0 

while en_marche:
    
    sleep(0.1)
    print("x")
    print(str(radioNavigation.x))
    print("y")
    print(str(radioNavigation.y))
    print("---")

    
    print(navigation.angleX)
    print(current_angle)


    

    #lidar.ScanLidar()
    #lidar.GetDistance(0)
    ##robot.Avancer()


    if(not robot.has_started):
        print("starting robot thread")
        robot.CalculerDistance(tabPosition[index] , tabAxes[index])
        robot.Start_Thread_Avancer()
        index += 1
        robot.has_started = True
    if(robot.arriver_position):
        print("arriver a la position")
        robot.Stop_Thread_Avancer()
        robot.Tourner(1)
        robot.arriver_position = False
        
    if(navigation.état == State.Rotation):
        print("rotating")
        if(abs(navigation.angleX - current_angle) >= 90):
            robot.Freiner()
            current_angle = navigation.angleX
            robot.has_started = False
        
    

        
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
