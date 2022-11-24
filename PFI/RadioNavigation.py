#Auteurs: Alexandre Carle et Louis-philippe Rousseau
import serial 
import time
class RadioNavigation:
    def __init__(self):
        self.ser = serial.Serial() 
        self.ser.port = '/dev/ttyACM0'
        self.ser.baudrate = 115200
        self.ser.open()
        self.data = None
        self.x = 0
        self.y = 0
        
    def demarrerCommunication(self):
        self.ser.write(b'\r\r') # séquence d’octets
        time.sleep(1)
        
    def getPosition(self):
        self.ser.write(b'lep\n') # Show pos. in CSV
        self.data = str(self.ser.readline())
        arrayString = self.data.split(',') 
        ##string.replace(oldvalue, newvalue)
        index = 0
        for pos in range(len(arrayString)):
            if(index == 1):
                self.x = float(pos)
            elif(index == 2):
                self.y = float(pos)
    def fermerConnection(self):
        self.ser.close()
    

        




