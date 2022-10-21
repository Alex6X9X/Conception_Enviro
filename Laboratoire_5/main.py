import cv2
import numpy as np
from Camera import Camera
from Console import Console


vcap = Camera()
console = Console()
arreter = False
    
frame = []

vcap._trouver_image_modele_(frame)

while not arreter:
    #vcap._read_()
    #console.afficher_image("Image" , vcap.image)
    choix = cv2.waitKey(33)
    if  choix == ord('q'):
        arreter = True  

#vcap._init_modele()

vcap._release_()
console.detruire_fenetres()