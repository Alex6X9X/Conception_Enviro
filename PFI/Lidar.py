import PyLidar3
import time
class Lidar:
    def __init__(self):
        self.port = "/dev/ttyUSB0"
        self.Obj = PyLidar3.YdLidarX4(self.port) 
        self.gen = None
        self.StartLidar()
        
    def StartLidar(self):
        if(self.Obj.Connect()):
            print(self.Obj.GetDeviceInfo())
            self.gen = self.Obj.StartScanning()
            
    def ScanLidar(self):
        while (...):         
            data = next(self.gen) # Dictionnaire: data[0:359] 
            print(data)               
            time.sleep(0.5)
            self.Obj.StopScanning()
            self.Obj.Disconnect()
        else:
            print("Erreur")
            self.Obj.Reset()    

        


