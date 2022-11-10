#Alexandre Carle et Louis-philippe Rousseau
#12 septembre 2022
#Dernier changement le 12 septembre 2022

from copier_tableau import copier_tableau

FENETRE = 10

def calculer_moyenne_mobile(nouvelle_distance , tableau_distance):
        
        tableau_distance.append(nouvelle_distance)
        
        if len(tableau_distance) >= FENETRE:
            del tableau_distance[0]
            return sum(tableau_distance)/len(tableau_distance)
        
        return None
    