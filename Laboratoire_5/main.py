import cv2
import numpy as np
from Camera import Camera
from Console import Console

CAMERA_FPS = 17 #~60 fps

vcap = Camera()
console = Console()
arreter = False


while not arreter:
    #vcap._read_()
    #console.afficher_image("Image" , vcap.image)
    vcap._trouver_image_modele_()
    console.afficher_image("Res", vcap.image)
    choix = cv2.waitKey(CAMERA_FPS)
    if  choix == ord('q'):
        arreter = True  

#vcap._init_modele()

vcap._release_()
console.detruire_fenetres()