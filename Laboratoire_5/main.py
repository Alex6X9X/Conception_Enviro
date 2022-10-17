import cv2
import numpy as np
from Camera import Camera


vcap = Camera()

while True:    
   vcap._creation_modele_()
   break

vcap.release()
cv2.destroyAllWindows()