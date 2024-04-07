#!/usr/bin/env python3
"""
fichier principal pour la detection des inclusions.
ce fichier est utilise pour les tests automatiques.
attention donc lors des modifications.
"""
<<<<<<< HEAD
from time import time
=======

>>>>>>> 95e479531d3ac3484181773d58f0c917e9775468
import sys
from tycat import read_instance
from geo import segment,point,polygon,quadrant
 
def is_inside(Point , polygon):
     x,y = Point.coordinates
     cont = 0
     for sengment in polygon.segments():
         head1,head2 = sengment.endpoints
         x1,y1 = head1.coordinates
         x2,y2 = head2.coordinates
         if (y<y1) != (y<y2) :
<<<<<<< HEAD
             if (x < x1 + (x1-x2)*((y-y1)/(y1-y2)) or x < x2 + ((y -y2)/(y1-y2))*(x1-x2)):
                 cont += 1
     return cont%2 == 1
 
def est_inclu(poly1,poly2):
     point = poly1.points[0]
     return is_inside(point,poly2)
 
def trouve_inclusions(polygones):
=======
             if (x < x1 + (x1-x2)*(y-y1)/(y1-y2) :
                 cont += 1
     return cont%2 == 1


 def trouve_inclusions(polygones):
>>>>>>> 95e479531d3ac3484181773d58f0c917e9775468
     """
     renvoie le vecteur des inclusions
     la ieme case contient l'indice du polygone
     contenant le ieme polygone (-1 si aucun).
     (voir le sujet pour plus d'info)
     """
     inclusions = []
<<<<<<< HEAD
     dic_aires = dict()
     n = len(polygones)
     for i in range (n):
         dic_aires[i] = abs(polygones[i].area())
     inclusions = [-1] * n
     for i in range (n):
        Liste_parents = []
        for j in range(n):
            if i != j and est_inclu(polygones[i],polygones[j]):
                Liste_parents.append([j,dic_aires[j]])
        if Liste_parents != []:
            indices_tries = sorted(range(len(Liste_parents)), key=lambda k: Liste_parents[k][1])
            inclusions[i] = Liste_parents[indices_tries[0]][0]
     
     return inclusions 
=======
     quadrant = []
     n = len(polygones)
     for i in range (n):
         polyq = polygones[i].bounding_quadrant()
         quadrant.append([polyq.max_coordinates[0],polyq.max_coordinates[1],polyq.min_coordinates[0],polyq.min_coordinates[1]])
     indices_tries = sorted(range(n), key=lambda k: quadrant[k].max_coordinates[0])
     inclusions = [-1] * n
     for j in range(n):
        i = j+1
        ind_j = indices_tries[j]
        while i < n :
            ind_i = indices_tries[i]
            if quadrant[ind_j][0]<quadrant[ind_i][0] and quadrant[ind_j][1]<quadrant[ind_i][1] and quadrant[ind_i][2]<quadrant[ind_j][2] and quadrant[ind_i][3]<quadrant[ind_j][3]:
                if is_inside(polygones[ind_j].points[0],polygones[ind_i]):
                    inclusions[ind_j] = ind_i
                    break
            i+=1

     return inclusions 
        
>>>>>>> 95e479531d3ac3484181773d58f0c917e9775468



def main():
    """
    charge chaque fichier .poly donne
    trouve les inclusions
    affiche l'arbre en format texte
    """
    for fichier in sys.argv[1:]:
        polygones = read_instance(fichier)
        inclusions = trouve_inclusions(polygones)
        print(inclusions)
<<<<<<< HEAD
        
def retourne_temps_naif(polygones):
    start_time = time()
    trouve_inclusions(polygones)
    end_time = time()
    execution_time = end_time - start_time
    return execution_time
=======
    
>>>>>>> 95e479531d3ac3484181773d58f0c917e9775468

if __name__ == "__main__":
    main()
