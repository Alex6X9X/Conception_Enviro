import cv2
import numpy as np
from Camera import Camera
from robot import Robot

vcap = Camera()
robot = Robot(vcap)

while True:    
    vcap._read_()
    #cv2.imshow("Image disc", vcap.image)
    robot.DeterminerMouvement()
    choix = cv2.waitKey(100)
    if  choix == ord('q'):
        break    


vcap.release()
#cv2.destroyAllWindows()