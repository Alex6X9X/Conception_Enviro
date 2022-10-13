#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 13 octobre 2022

import cv2
import numpy as np
from Camera import Camera
from robot import Robot
from Console import Console

vcap = Camera()
robot = Robot(vcap)
console = Console()

arreter = False

while not arreter:    
    vcap._read_()
    console.afficher_image("Labo 4", vcap.image)
    robot.DeterminerMouvement()
    choix = cv2.waitKey(125)
    if  choix == ord('q'):
        arreter = True   

vcap._release_()
console.detruire_fenetres()