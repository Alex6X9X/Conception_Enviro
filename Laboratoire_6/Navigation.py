import threading
from time import sleep
from icm20948 import ICM20948
from calculer_moyenne_mobile import calculer_moyenne_mobile
from State import State
G = 9,80665 #m/s2
class Navigation : 
    
    def __init__(self , imu , robot):
        self.état = 0
        self.thread_calcul_position = threading.Thread(target = self._calculer_position , args=())
        self.en_marche = True
        self.ax= None 
        self.ay= None 
        self.az= None
        self.gx= None
        self.gy= None
        self.gz= None
        self.mx= None
        self.my= None
        self.mz= None
        self.imu = imu
        self.robot = robot
        self.thread_calcul_position.start()
    def _calculer_position(self):
        while(self.en_marche):
            sleep(0.05)
            if(self.état == State.Immobile):
                ##À l’arrêt: le fil calcule les biais de gx et de ay en utilisant une moyenne fenêtrée. 
                print("immobile")
            elif(self.état ==  State.Rotation):
                ##En rotation: le fil calcule la nouvelle orientation du robot en tenant compte du temps écoulé entre deux mesures et le biais calculé pour gx. 
                print("rotation")
            elif(self.état ==  State.Translation):
                ##En translation: le fil calcule la nouvelle position en y du robot en tenant compte du temps écoulé entre deux mesures et le biais calculé pour ay. 
                print("translation")

    def _get_gyro_data(self):
        self.ax, self.ay, self.az, self.gx, self.gy, self.gz = self.imu.read_accelerometer_gyro_data()
        self.mx, self.my, self.mz = self.imu.read_magnetometer_data()
