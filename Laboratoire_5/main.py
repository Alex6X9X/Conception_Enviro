import cv2
import numpy as np
from Camera import Camera


vcap = Camera()

 
#vcap._creation_modele_()
vcap._trouver_image_modele_()


vcap.vcap.release()
cv2.destroyAllWindows()