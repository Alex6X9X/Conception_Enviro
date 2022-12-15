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


en_marche = True

imu = ICM20948()
angle = 0
navigation = Navigation(imu, en_marche)
radioNavigation = RadioNavigation(en_marche)
lidar = Lidar(en_marche)
robot = Robot(navigation , radioNavigation, lidar, en_marche)
has_started_turning = False
init_angle_robot = True

beggining_of_circuit = True

##tabPosition = [(6 , -0.34), (7.94 , 0.27) , (8.15 , 2.63) , (6.2 , 2.78)]
tabPosition = [(12.20 , 5.80) , (12.20 , 3.70), (10.5, 3.70), (10.5, 5.7)]
index = 0
has_started = False
sleep(7)
robot.initialiserPosition()
while(en_marche):
    if(not has_started):
        print("start thread_avancer")
        robot.Start_Thread_Avancer(tabPosition[index][0], tabPosition[index][1], angle)
        has_started = True
        print(radioNavigation.x)
        print(radioNavigation.y)
    if(robot.arriver_position and has_started):
        if(not has_started_turning):
            robot.Stop_Thread_Avancer()
            print("yo")
            index += 1
            angle = robot.CalculerAngle(tabPosition[index][0], robot.x, tabPosition[index][1], robot.y)
            print(angle)
            robot.Tourner(angle)
      
            
            
            has_started_turning = True
        ##verif angle 90
        print("nav",navigation.angleX)
        print("robot",robot.angleX)
        print("calcul", navigation.angleX <= robot.angleX - 90)
        if(navigation.angleX >= robot.angleX + 90 or navigation.angleX <= robot.angleX - 90):
            robot.Freiner()
            robot.angleX == navigation.angleX
            has_started = False


sleep(10)
     
        
radioNavigation.thread_get_position.join()
radioNavigation.fermerConnection()

    

#navigation.thread_affichage.join()
