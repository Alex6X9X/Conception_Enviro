#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

from Dell import Dell
import gpiozero
from sonar import Sonar
import numpy as np
import cv2


PORT_DEL_JAUNE = 10
PORT_DEL_VERTE = 9
SGT = 8   #Sonar Gauche Trigger...
SDT = 21  
SGE = 25  #Sonar Gauche Echo...
SDE = 20

arreter = False
sonars = Sonar(SGT, SDT, SGE, SDE, arreter)
del_jaune = Dell(PORT_DEL_JAUNE, sonars, 'g', arreter)
del_verte = Dell(PORT_DEL_VERTE, sonars, 'd', arreter)

org = (50,50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)
line_type = 2

img = np.zeros((512,512,3),np.uint8)

img_2 = cv2.putText(img, 
            "Sonar ", 
            org, 
            font, 
            font_scale, 
            font_color, 
            line_type,
            cv2.LINE_AA)  

cv2.imshow('Labo 1', img_2)  
#sonars.Demarrer()
#sonars.Arreter()