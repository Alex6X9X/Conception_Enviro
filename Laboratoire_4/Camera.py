import cv2
import numpy as np

WIDTH = 320
HEIGHT = 240
PORT = 0
TEINTE = 176
SAT_MIN =16
SAT_MAX =202
VAL_MIN = 64
VAL_MAX = 255
DELTA = 3

class Camera:
    
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT)
        if not self.vcap.isOpened():
            print("Erreur lors de l'ouverture de la caméra")
            exit()
        self.frame_hsv = None
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        
    def _read_(self):
        self.ok , self.image = self.vcap.read()
        self.image =cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        teinte_min = np.array([TEINTE - DELTA, SAT_MIN, VAL_MIN])
        teinte_max = np.array([TEINTE + DELTA, SAT_MAX, VAL_MAX])
        self.image = cv2.inRange(self.image, teinte_min, teinte_max)

        return self.image
    
    

