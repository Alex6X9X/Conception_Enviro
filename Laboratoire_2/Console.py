#Alexandre Carle et Louis-philippe Rousseau
#9 septembre 2022
#Dernier changement le 31 août 2022

import numpy as np
import cv2

LARGEUR = 512
GRANDEUR = 700
POSITION_X = 40
POSITION_Y = 40
SAUT_LIGNE = 35
SAUT_COLONNE = 100

class Console:
    
    def __init__(self):
        self.img = np.zeros((LARGEUR,GRANDEUR,3),np.uint8)
        self.x = POSITION_X
        self.y = POSITION_Y
        
    def afficher(self):
        cv2.imshow('Labo 2', self.img)
        
    def afficher_distances(self, distance, dir):
        
        org = (self.x, self.y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_color = (255, 255, 255)
        line_type = 1
        
        if(distance != None):
            self.img = cv2.putText(self.img, 
                                    "Sonar " + dir + " : %.2f cm" % distance, 
                                    org, 
                                    font, 
                                    font_scale, 
                                    font_color, 
                                    line_type)   
            
        if(self.y >= LARGEUR):
            cv2.destroyAllWindows()
            self.afficher()
        else:
            self.y = self.y + SAUT_LIGNE
        cv2.imshow('Labo 2', self.img)