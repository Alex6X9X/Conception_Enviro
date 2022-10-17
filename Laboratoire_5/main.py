import cv2
import numpy as np
from Camera import Camera


vcap = Camera()

while True:    
    vcap._read_()

    choix = cv2.waitKey(125)
    if  choix == ord('q'):
        break    


vcap.release()
cv2.destroyAllWindows()