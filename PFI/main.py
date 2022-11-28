#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 14 novembre 2022

from time import sleep
from Robot import Robot
from Navigation import Navigation
from icm20948 import ICM20948
from RadioNavigation import RadioNavigation
from Lidar import Lidar
en_marche = True

imu = ICM20948()

navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
radioNavigation.demarrerCommunication()
radioNavigation.thread_get_position.start()
robot = Robot(navigation , radioNavigation, en_marche)
robot.initialiserPosition()
#lidar = Lidar(en_marche)

#robot.Tourner(0)
#if(navigation.angleX < -90):
#    robot.Freiner()
    
tabPosition = [2 , 6 , 8, 9]
tabAxes = ['X' , 'Y' , 'X' , 'Y']
index = 0 
while en_marche:
    sleep(0.1)
    print("x")
    print(radioNavigation.x)
    print("y")
    print(radioNavigation.y)
    print("---")
    #lidar.ScanLidar()
    #lidar.GetDistance(0)
    ##robot.Avancer()


    ##if(not robot.has_started):
      ##  robot.CalculerDistance(tabPosition[index] , tabAxes[index])
      ##  robot.Start_Thread_Avancer()
      ##  index += 1
      ##  robot.has_started = True
    ##if(robot.arriver_position):
      ##  robot.Stop_Thread_Avancer()
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
