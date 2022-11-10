#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 27 octobre 2022

import numpy as np
import cv2
import time

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
            distance_droite = round(distance_droite, 2)
            distance_gauche = round(distance_gauche, 2)
            self.img = cv2.putText(img, 
                                    "Sonar droite : " + str(distance_droite) + " cm || Sonar gauche " + str(distance_gauche) + " cm",
                                    org, 
                                    font, 
                                    font_scale, 
                                    font_color, 
                                    line_type)   
            
        self.afficher_image("Labo 2", img)
        
    def afficher_image(self, titre, image):
        cv2.imshow(titre, image)
    
    def detruire_fenetres(self):
        cv2.destroyAllWindows()
        
    def afficher_donnees(self, angleX, posY, en_marche):
        while(en_marche):
            time.sleep(0.1)
            print("Angle X: " + str(angleX))
            print("Position Y: " + str(posY))