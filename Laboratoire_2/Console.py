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
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_color = (255, 255, 255)
        line_type = 1
        
        if(distance != None):
            if dir == 'gauche':
                self.img = cv2.putText(self.img, 
                                        "Sonar " + dir + " : %.2f cm" % distance, 
                                        (self.x, self.y), 
                                        font, 
                                        font_scale, 
                                        font_color, 
                                        line_type)   
            elif dir == 'droite':
                self.img = cv2.putText(self.img, 
                                        "Sonar " + dir + " : %.2f cm" % distance, 
                                        (self.x + 20, self.y + 20), 
                                        font, 
                                        font_scale, 
                                        font_color, 
                                        line_type) 
            else:
                #Cas extrême
                return -1
        self.afficher()