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

console.afficher_image("Labo 4", np.zeros((300,300,3),np.uint8))

while not arreter:    
    vcap._read_()
    robot.DeterminerMouvement()
    choix = cv2.waitKey(100)
    if  choix == ord('q'):
        arreter = True   


vcap.release()
console.detruire_fenetres()