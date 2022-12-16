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
##lidar.thread_scan_lidar.start()
robot = Robot(navigation , radioNavigation, lidar, en_marche)
has_started_turning = False
init_angle_robot = True

beggining_of_circuit = True

##tabPosition = [(6 , -0.34), (7.94 , 0.27) , (8.15 , 2.63) , (6.2 , 2.78)]
tabPosition = [(6 , 0.60) , (8.20 , 0.9), (8.20, 2.45), (6.40, 2.25)]
index = 0
has_started = False
sleep(5)
robot.initialiserPosition()
while(en_marche):
    
    if(not has_started):
        print("start thread_avancer")
        robot.Start_Thread_Avancer(tabPosition[index][0], tabPosition[index][1], angle)
        has_started = True
        print(robot.arriver_position)

   
    if(robot.arriver_position):
        if(not has_started_turning):
            robot.Stop_Thread_Avancer()
            print("commence à tourner" , robot.arriver_position)
            index += 1
            #angle = robot.CalculerAngle(tabPosition[index][0], robot.x, tabPosition[index][1], robot.y)
            robot.Tourner(1)
            has_started_turning = True
            
        ##verif angle 90
        if(navigation.angleX >= robot.angleX + 89 or navigation.angleX <= robot.angleX - 89 and has_started_turning):
            robot.Freiner()
            print('-----------------------------------------------------------------------------------------')
            robot.angleX = navigation.angleX
            has_started = False
            has_started_turning = False
            
    if(index == len(tabPosition)):
        en_marche = False
        robot.Freiner()


sleep(10)
     
        
radioNavigation.thread_get_position.join()
radioNavigation.fermerConnection()

    

#navigation.thread_affichage.join()
