#Alexandre Carle et Louis-philippe Rousseau
#29 août 2022
#Dernier changement le 11 septembre 2022

from time import sleep
from Console import Console
from Dell import Dell
from sonar import Sonar
import cv2

PORT_DEL_JAUNE = 10
PORT_DEL_VERTE = 9
SGT = 8   #Sonar Gauche Trigger...
SDT = 21  
SGE = 25  #Sonar Gauche Echo...
SDE = 20

arreter = False
sonar_gauche = Sonar(SGT, SDT, SGE, SDE, arreter)
sonar_droite = Sonar(SGT, SDT, SGE, SDE, arreter)
del_jaune = Dell(PORT_DEL_JAUNE, sonar_gauche, 'g', arreter)
del_verte = Dell(PORT_DEL_VERTE, sonar_droite, 'd', arreter)
console = Console()

console.afficher_distances(None, None)

print("Appuyer sur la touche 'x' pour quitter le programme...")

#Démarrage des threads
sonars.Demarrer()
del_jaune.Demarrer()
del_verte.Demarrer()

while (not arreter):
    key = cv2.waitKey(100)
        
    sleep(0.1)        
    console.afficher_distances(sonars.distance_courante_droite, sonars.distance_courante_gauche)
    
    if key == ord('x'):
        arreter = True
        sonars.arreter = arreter
        del_jaune.arreter = arreter
        del_verte.arreter = arreter
        
        #Arrêt des threads
        sonars.Arreter()
        del_jaune.Arreter()
        del_verte.Arreter()
        
