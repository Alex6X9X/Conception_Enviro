from copier_tableau import copier_tableau

FENETRE = 10

def calculer_moyenne_mobile(nouvelle_distance , tableau_distance):
        
        tableau_distance.append(nouvelle_distance)
        
        if len(tableau_distance) >= FENETRE:
            temp_tab = copier_tableau(tableau_distance)
            temp_min = min(temp_tab)
            temp_max = max(temp_tab) 
            temp_tab.remove(temp_min)
            temp_tab.remove(temp_max)
            del tableau_distance[0]
            return sum(temp_tab)/len(temp_tab)
        
        return None
    