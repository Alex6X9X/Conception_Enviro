#Auteurs: Alexandre Carle et Louis-philippe Rousseau
import serial 
import time
import threading
class RadioNavigation:
    def __init__(self , en_marche):
        self.ser = serial.Serial() 
        self.ser.port = '/dev/ttyACM0'
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS 
        self.ser.parity =serial.PARITY_NONE 
        self.ser.stopbits = serial.STOPBITS_ONE 
        self.ser.timeout = 1
        self.ser.open()
        print("RadioNavigation")
        self.ser.write(b'\r\r') # séquence d’octets
        time.sleep(1)
        self.ser.write(b'lep\r')
        self.en_marche = en_marche
        self.data = None
        self.x = 0
        self.y = 0
        self.thread_get_position = threading.Thread(target = self.getPosition , args=())
        
    def demarrerCommunication(self):
        pass
        
    def getPosition(self):
        self.ser.open()
        while(self.en_marche):
            time.sleep(0.1)
            self.data = str(self.ser.readline())
            print(self.data)
            arrayString = self.data.split(',') 
            ##string.replace(oldvalue, newvalue)
            if(len(arrayString) > 1):
                self.x = float(arrayString[1])
                self.y = float(arrayString[2])
        self.ser.close()
    def fermerConnection(self):
        self.ser.close()
    

        




