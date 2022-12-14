#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 19 décembre 2022
import PyLidar3
import time
import threading


class Lidar:
    def __init__(self, en_marche):
        self.port = "/dev/ttyUSB0"
        self.Obj = PyLidar3.YdLidarX4(self.port) 
        self.gen = None
        self.data = None
        self.en_marche = en_marche
        self.thread_scan_lidar = threading.Thread(target = self.ScanLidar , args=())

        

    def ScanLidar(self):
        if(self.Obj.Connect()):
            self.gen = self.Obj.StartScanning()
            while (self.en_marche):         
                self.data = next(self.gen) # Dictionnaire: data[0:359]             
                time.sleep(0.5)

            self.Obj.StopScanning()
            self.Obj.Disconnect()    
        else:
            print("Erreur")
            self.Obj.Reset() 
    def GetDistance(self , distance):
        if(self.data != None):
            return self.data[distance]
        

        


