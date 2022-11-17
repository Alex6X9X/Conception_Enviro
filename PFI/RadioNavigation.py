#Auteurs: Alexandre Carle et Louis-philippe Rousseau et Guillaume Légaré
import serial 
import time
import threading
class RadioNavigation:
    def __init__(self):
        self.ser = serial.Serial() 
        self.ser.port = '/dev/ttyACM0'
        self.ser.baudrate = 115200
        self.ser.open()
        self.data = None
        self.x =0
        self.y =0
        self.thread_get_position = threading.Thread(target = self.getPosition , args=())
        self.thread_get_position.start()
        self.en_marche = True
        
        
    def demarrerCommunication(self):
        self.ser.write(b'\r\r') # séquence d’octets
        time.sleep(1)
        self.ser.write(b'lep\n') # Show pos. in CSV
    def getPosition(self):
        while(self.en_marche):
            time.sleep(0.1)
            self.data = str(self.ser.readline())
            arrayString = self.data.split(',') 
            ##string.replace(oldvalue, newvalue)
            index = 0
            for pos in range(len(arrayString)):
                if(index == 1):
                    self.x = float(pos)
                elif(index == 2):
                    self.y = float(pos)
            self.printPosition()
    
        
    def printPosition(self):
        print("position en x" + self.x)
        print("position en y" + self.y)
    def fermerConnection(self):
        self.ser.close()
    

        




