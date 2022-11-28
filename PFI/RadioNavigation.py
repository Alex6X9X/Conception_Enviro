#Auteurs: Alexandre Carle et Louis-philippe Rousseau
import serial 
import time
import threading
class RadioNavigation:
    def __init__(self , en_marche):
        self.ser = serial.Serial() 
        self.ser.port = '/dev/ttyACM0'
        self.ser.baudrate = 115200
        self.ser.open()
        self.en_marche = en_marche
        self.data = None
        self.x = 0
        self.y = 0
        self.thread_get_position = threading.Thread(target = self.getPosition , args=())
        
    def demarrerCommunication(self):
        print("RadioNavigation")
        self.ser.write(b'\r\r') # séquence d’octets
        time.sleep(1)
        
    def getPosition(self):
        while(self.en_marche):
            time.sleep(0.1)
            self.ser.write(b'lep\n') # Show pos. in CSV
            self.data = str(self.ser.readline())
            arrayString = self.data.split(',') 
            ##string.replace(oldvalue, newvalue)
            index = 0
            for pos in range(len(arrayString)):
                
                if(index == 1):
                    self.x = pos
                elif(index == 2):
                    self.y = pos
    def fermerConnection(self):
        self.ser.close()
    

        




