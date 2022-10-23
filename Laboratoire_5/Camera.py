
from email.mime import image
import cv2
import numpy as np
from Console import Console

WIDTH = 320
HEIGHT = 240
PORT = 0
EPAISSEUR = 2

SEUIL_ACCEPTATION = 0.79

DELTA_ROI = 5

class Camera:
    
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT)
        if not self.vcap.isOpened():
            print("Erreur lors de l'ouverture de la caméra")
            exit()
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        self.contours = None
        self.image = None
        self.min_val = None
        self.max_val = None
        self.min_loc = None
        self.max_loc = None
        self.frame_roi = []
        self.x = 0
        self.y = 0
        self.l = 0
        self.h = 0
        self.ymin = None
        self.ymax = None
        self.xmin = None
        self.xmax = None
        
    def _read_(self):
        self.ok , self.image = self.vcap.read()
        #return self.image
        
    def _release_(self):
        self.vcap.release()
        
    def _draw_rectangle(self,x,y,l,h, r, g, b):
        #print(str(x) + " " +  str(y) + " " + str(x+l) + " "  + str(y+h))
        cv2.rectangle(self.image, (x,y), (x+l,y+h), (r, g, b), EPAISSEUR) 
        
    def _init_modele(self):
        self._read_()
        modele = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("image_modele.bmp", modele)
    
    def _trouver_image_modele_(self):
        self._read_()
        modele_minimise = cv2.imread("image_modele_version2.bmp" , 0)
        mask = cv2.imread("background.png" , 0)
        
        image_gris = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(image_gris, modele_minimise, cv2.TM_CCOEFF_NORMED  , None , mask)
        self.min_val, self.max_val, self.min_loc, self.max_loc = cv2.minMaxLoc(res)
        print("Max_Val dans le frame :" + str(self.max_val))
        if(self.max_val < SEUIL_ACCEPTATION):
            res = cv2.matchTemplate(image_gris, modele_minimise, cv2.TM_CCOEFF_NORMED , None , mask)
            self.min_val, self.max_val, self.min_loc, self.max_loc = cv2.minMaxLoc(res)
        #print(self.max_loc)
        self._def_ROI_()
        (startX, startY) = self.max_loc
        print(startX, startY)
        self.x = startX
        self.y = startY
        self.l = modele_minimise.shape[1]
        self.h = modele_minimise.shape[0]
        
        
        if(self.x != 0 and self.y != 0):
            #La cible
            self._draw_rectangle(self.x, self.y, self.l, self.h, 255, 0, 0)
            
            #Le frame ROI
            self._draw_rectangle(self.xmin, self.ymin, self.xmax, self.ymax, 20, 170, 60)

    def _def_ROI_(self):
        self.ymin = self.y - DELTA_ROI
        self.xmin = self.x - DELTA_ROI
        self.ymax = self.h + DELTA_ROI
        self.xmax = self.l + DELTA_ROI
        self.frame_roi = self.image[self.ymin:self.ymax, self.xmin:self.xmax]

    def _reset_ROI(self):
        self.ymin = None
        self.xmin = None
        self.ymax = None
        self.xmax = None
        self.frame_roi = self.image[self.ymin:self.ymax, self.xmin:self.xmax]

    def _reset_values(self):
        self.x = 0
        self.y = 0


        



    
    

