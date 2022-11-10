#Auteurs: Alexandre Carle et Louis-philippe Rousseau
#Dernier changement 10 novembre 2022

FENETRE = 10

def calculer_moyenne_mobile(nouvelle_distance , tableau_distance):
        
        tableau_distance.append(nouvelle_distance)
        
        if len(tableau_distance) >= FENETRE:
            del tableau_distance[0]
            return sum(tableau_distance)/len(tableau_distance)
        
        return None
    