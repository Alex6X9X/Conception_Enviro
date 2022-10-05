
import cv2
import numpy as np

WIDTH = 320
HEIGHT = 240
PORT = 0
TEINTE = 0
SAT_MIN =120
SAT_MAX = 213
VAL_MIN = 107
VAL_MAX = 255
DELTA = 10
EPAISSEUR = 2

MIN_CENTRE = 100
MAX_CENTRE = 200

MIN_AIRE_BALLE = 150

MAX_AIRE_BALLE = 8000

class Camera:
    
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT)
        if not self.vcap.isOpened():
            print("Erreur lors de l'ouverture de la caméra")
            exit()
        self.frame_hsv = None
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        self.contours = None
        self.aire_balle = None
        self.x_balle = None
        self.y_balle = None
        
    def _read_(self):
        self.ok , self.image = self.vcap.read()
        self.image =cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        teinte_min = np.array([TEINTE - DELTA, SAT_MIN, VAL_MIN])
        teinte_max = np.array([TEINTE + DELTA, SAT_MAX, VAL_MAX])
        self.image = cv2.inRange(self.image, teinte_min, teinte_max)
        
        self._contour_()
        return self.image
    def _determiner_position_(self):
        
        
        if(self.aire_balle != None and  self.aire_balle < MAX_AIRE_BALLE and self.aire_balle > MIN_AIRE_BALLE):
            
            if(self.x_balle < MIN_CENTRE):
                return "left"
            elif(self.x_balle > MAX_CENTRE):
                return "right"
            else:
                return "avancer"
        else:
            return "stop"
       
        

    def _contour_(self):
        self.contours, _ = cv2.findContours(self.image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        plus_grand_aire = 0
        coordoné = []
        if(len(self.contours) == 0):
            self.aire_balle =0
        for c in self.contours:
            x, y, l, h = cv2.boundingRect(c)
            air_rect = l * h
            if(air_rect > plus_grand_aire):
                plus_grand_aire = air_rect
                self.x_balle = x + l/2
                self.y_balle = y + h/2
                self.aire_balle = plus_grand_aire
                coordoné.clear()
                coordoné.append(x)
                coordoné.append(y)
                coordoné.append(l)
                coordoné.append(h)

        if(len(coordoné) > 0):
            self._draw_rectangle(coordoné[0] , coordoné[1], coordoné[2], coordoné[3])   
        
            
        self._draw_contour_()
        

    def _draw_contour_(self ):
        cv2.drawContours(self.image, self.contours, -1, (0,0,255), EPAISSEUR)
    def _draw_rectangle(self,x,y,l,h):
        cv2.rectangle(self.image, (x,y), (x+l,y+h), (255, 165, 0), EPAISSEUR) 




    
    

