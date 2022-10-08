from multiprocessing.heap import Arena
import cv2
import numpy as np
from Camera import Camera
from robot import Robot
from Console import Console

vcap = Camera()
robot = Robot(vcap)
console = Console()

arreter = False

#np.zeros((150,150,3),np.uint8)

while not arreter:    
    vcap._read_()
    console.afficher_image("Labo 4", np.zeros((150,150,3),np.uint8))
    robot.DeterminerMouvement()
    choix = cv2.waitKey(125)
    if  choix == ord('q'):
        arreter = True   

vcap._release_()
console.detruire_fenetres()