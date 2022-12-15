#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 13 octobre 2022

import cv2
import numpy as np

WIDTH = 320
HEIGHT = 240
PORT = 0
TEINTE = 0
SAT_MIN = 120
SAT_MAX = 213
VAL_MIN = 107
VAL_MAX = 255
DELTA = 10
EPAISSEUR = 2
vcap = cv2.VideoCapture(0) # caméra 0
if not vcap.isOpened():
    print("Impossible d'ouvrir la caméra vidéo")
    exit()
# Modification de la résolution de 2592x1944 à 320x240
# Notez le rapport de 16:9 entre la largeur et la hauteur.
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) 
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
ok, image = vcap.read() 
cv2.imshow("Image", image)
cv2.waitKey(0)  	# Attend indéfiniment qu’une touche soit pressée
vcap.release()
cv2.destroyAllWindows()



