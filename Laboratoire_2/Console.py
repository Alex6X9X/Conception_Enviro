#Alexandre Carle et Louis-philippe Rousseau
#9 septembre 2022
#Dernier changement le 11 septembre 2022

import numpy as np
import cv2

LARGEUR = 512
GRANDEUR = 700
POSITION_X = 40
POSITION_Y = 40

class Console:
    
    def __init__(self):
        self.x = POSITION_X
        self.y = POSITION_Y
        
    def afficher_distances(self, distance_droite, distance_gauche):
        img = np.zeros((LARGEUR,GRANDEUR,3),np.uint8)
        
        org = (self.x, self.y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_color = (255, 255, 255)
        line_type = 1
        
        if(distance_droite != None and distance_gauche != None):
            self.img = cv2.putText(img, 
                                    "Sonar droite : " + str(distance_droite) + " cm\n Sonar gauche " + str(distance_gauche) + " cm",
                                    org, 
                                    font, 
                                    font_scale, 
                                    font_color, 
                                    line_type)   
            
        cv2.imshow('Labo 2', img)