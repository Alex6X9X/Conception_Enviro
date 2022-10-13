from multiprocessing.heap import Arena
import cv2
import numpy as np
from Camera import Camera
from robot import Robot

vcap = Camera()
robot = Robot(vcap)

arreter = False

while not arreter:    
    vcap._read_()
    robot.DeterminerMouvement()
    choix = cv2.waitKey(125)
    if  choix == ord('q'):
        arreter = True   

vcap._release_()