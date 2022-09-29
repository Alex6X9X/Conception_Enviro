import cv2
import numpy as np
import Camera 


vcap = Camera()

while True:    
    vcap._read_()
    cv2.imshow("Image disc", vcap.image)

    choix = cv2.waitKey(125)
    if  choix == ord('q'):
        break    


vcap.release()
cv2.destroyAllWindows()