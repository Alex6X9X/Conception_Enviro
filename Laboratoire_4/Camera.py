import cv2;

WIDTH = 320
HEIGHT = 240
PORT = 0

class Camera:
    
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT)
        if not self.vcap.isOpened():
            print("Erreur lors de l'ouverture de la caméra")
            exit()
        self.frame_hsv = None
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        
    def _read_(self):
        self.ok , self.image = self.vcap.read()
        self.image =cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        return self.ok,self.image
    
    

