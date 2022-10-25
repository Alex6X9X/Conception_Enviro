
from email.mime import image
from socket import AI_MASK
import cv2
import numpy as np
from Console import Console

WIDTH = 320
HEIGHT = 240
PORT = 0
EPAISSEUR = 2

SEUIL_ACCEPTATION = 0.76

DELTA_ROI = 10

class Camera:
    
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT)
        if not self.vcap.isOpened():
            print("Erreur lors de l'ouverture de la caméra")
            exit()
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
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
        ok , self.image = self.vcap.read()
        
    def _release_(self):
        self.vcap.release()
        
    def _draw_rectangle(self, x, y, l, h, r, g, b):
        cv2.rectangle(self.image, (x,y), (l,h), (r, g, b), EPAISSEUR) 
        
    def _init_modele(self):
        self._read_()
        modele = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("image_modele.bmp", modele)
    
    def _trouver_image_modele_(self):
        self._read_()
        template_img = cv2.imread("image_modele_version2.bmp" , 0)
        mask = cv2.imread("background.png" , 0)
        
        if(self.frame_roi == []):
            self._trouver_cible(template_img, mask)
            self._set_attributes_(template_img)
            self._def_ROI_()
        else:
            self._set_attributes_(template_img)
            self._def_ROI_()
            res = cv2.matchTemplate(self.frame_roi, template_img, cv2.TM_CCOEFF_NORMED, None , mask)
            self.min_val, self.max_val, self.min_loc, self.max_loc = cv2.minMaxLoc(res)
            
        if(self.max_val < SEUIL_ACCEPTATION):
            print("refait verif dans image")
            self._trouver_cible(template_img, mask)
             
        #La cible
        self._draw_rectangle(self.x, self.y, (self.x + self.l), (self.y+self.h), 255, 0, 0)
        
        if(self.frame_roi != []):
            #Le frame ROI
            self._draw_rectangle(self.xmin, self.ymin, self.xmax, self.ymax, 20, 170, 60)
            
    def _trouver_cible(self, template_img, mask):
        image_gris = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(image_gris, template_img, cv2.TM_CCOEFF_NORMED, None , mask)
        self.min_val, self.max_val, self.min_loc, self.max_loc = cv2.minMaxLoc(res)
    
    def _set_attributes_(self , template_img):
        print("Set attribute")
        (startX, startY) = self.max_loc
        self.x = startX
        self.y = startY
        self.l = template_img.shape[1] 
        self.h = template_img.shape[0]
        
    def _def_ROI_(self):
        print("defROI")
        self.ymin = self.y - DELTA_ROI
        self.xmin = self.x - DELTA_ROI
        self.ymax = self.ymin + self.h + DELTA_ROI * 2
        self.xmax = self.xmin + self.l + DELTA_ROI * 2
        
        self._corriger_pos_ROI()
        
        self.frame_roi = self.image[self.ymin:self.ymax, self.xmin:self.xmax]
        self.frame_roi = cv2.cvtColor(self.frame_roi, cv2.COLOR_BGR2GRAY)
    
    def _corriger_pos_ROI(self):
        if(self.ymin < 0):
            self.ymin = 0
        if(self.xmin < 0):
            self.xmin = 0
        if(self.ymax > HEIGHT):
            self.ymax = HEIGHT - 10
        if(self.xmax > WIDTH):
            self.xmax = WIDTH - 10
    
       

        



    
    

