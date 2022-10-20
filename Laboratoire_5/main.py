import cv2
import numpy as np
from Camera import Camera


vcap = Camera()
arreter = False
    
frame = []
#vcap._creation_modele_()

vcap._trouver_image_modele_(frame)

while not arreter:
    choix = cv2.waitKey(100)
    if  choix == ord('q'):
        arreter = True  

vcap.vcap.release()
cv2.destroyAllWindows()