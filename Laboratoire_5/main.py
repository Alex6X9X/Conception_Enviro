#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 27 octobre 2022

import cv2
import numpy as np
from Camera import Camera
from Console import Console

vcap = Camera()
console = Console()
arreter = False


while not arreter:
    #vcap._read_()
    #console.afficher_image("Image" , vcap.image)
    vcap._trouver_cible_()
    console.afficher_image("Labo 5", vcap.image)
    choix = cv2.waitKey(16)
    if  choix == ord('q'):
        arreter = True  

#vcap._init_modele()

vcap._release_()
console.detruire_fenetres()