#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 31 août 2022

from Dell import Dell
import gpiozero
from sonar import Sonar
import cv2

PORT_DEL_JAUNE = 10
PORT_DEL_VERTE = 9
SGT = 8   #Sonar Gauche Trigger...
SDT = 21  
SGE = 25  #Sonar Gauche Echo...
SDE = 20

arreter = False
sonars = Sonar(SGT, SDT, SGE, SDE, arreter)
del_jaune = Dell(PORT_DEL_JAUNE, sonars, 'g', arreter)
del_verte = Dell(PORT_DEL_VERTE, sonars, 'd', arreter)

print("Appuyer sur la touche 'x' pour quitter le programme...")

#Démarrage des threads
sonars.Demarrer()
del_jaune.Demarrer()
del_verte.Demarrer()

while (not arreter):
    key = cv2.waitKey(100)
    
    if key == ord('x'):
        print("C'est fini!")
        arreter = True
        sonars.arreter = arreter
        del_jaune.arreter = arreter
        del_verte.arreter = arreter
        
