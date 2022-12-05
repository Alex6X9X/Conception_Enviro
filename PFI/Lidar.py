import PyLidar3
import time

#Distance en mm
FACTEUR_CONVERSION = 0.001

class Lidar:
    def __init__(self, en_marche):
        self.port = "/dev/ttyUSB0"
        self.Obj = PyLidar3.YdLidarX4(self.port) 
        self.gen = None
        self.data = None
        self.en_marche = en_marche
        self.StartLidar()
        
    def StartLidar(self):
        if(self.Obj.Connect()):
            print(self.Obj.GetDeviceInfo())
            self.gen = self.Obj.StartScanning()
            
    def ScanLidar(self):
        while (not self.en_marche):         
            self.data = next(self.gen) # Dictionnaire: data[0:359] 
            print(self.data)               
            time.sleep(0.5)
            self.Obj.StopScanning()
            self.Obj.Disconnect()
        else:
            print("Erreur")
            self.Obj.Reset() 
    def GetDistance(self, angle):
        return self.ConversionMetre(self.data[angle])
    
    def ConversionMetre(self, distance):
        return distance * FACTEUR_CONVERSION
        

        


