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
        self.ser.close()
        self.en_marche = en_marche
        self.data = None
        self.x = 0
        self.y = 0
        self.thread_get_position = threading.Thread(target = self.getPosition , args=())
        print("start thread")
        self.thread_get_position.start()
    def getPosition(self):
        self.ser.open()
        self.ser.write(b'lep\r')
        self.ser.close()
        while(self.en_marche):
            time.sleep(0.05)
            #compteur = time.perf_counter()
            self.ser.open()
            self.data = str(self.ser.readline())
            self.ser.close()
            #print(time.perf_counter() - compteur)
            arrayString = self.data.split(',') 
            ##string.replace(oldvalue, newvalue)
            if(len(arrayString) > 1):
                if(arrayString[1] != '' or arrayString[2] != ''):
                    self.x = float(arrayString[1])
                    self.y = float(arrayString[2])
                    
                    
       
    def fermerConnection(self):
        self.ser.close()
    

        




