#!/usr/bin/env python3
"""
fichier principal pour la detection des inclusions.
ce fichier est utilise pour les tests automatiques.
attention donc lors des modifications.
"""
from time import time
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
             if x < x1 + (x1-x2)*(y-y1)/(y1-y2) :
                 cont += 1
     return cont%2 == 1
 

def quadrant_inclus(quadrant1, quadrant2):
    """
    Vérifie si quadrant1 est strictement inclus dans quadrant2.
    """
    for min1, min2, max1, max2 in zip(quadrant1.min_coordinates, quadrant2.min_coordinates,
                                       quadrant1.max_coordinates, quadrant2.max_coordinates):
        if not (min2 < min1 < max1 < max2):
            return False
    return True

 
def trouve_inclusions(polygones):
     """
     renvoie le vecteur des inclusions
     la ieme case contient l'indice du polygone
     contenant le ieme polygone (-1 si aucun).
     (voir le sujet pour plus d'info)
     """
     n = len(polygones)
     inclusions = []
     quadrant = []
     dic_aires = dict()
     for i in range (n):
         dic_aires[i] = abs(polygones[i].area())
     for i in range (n):
         quadrant.append(polygones[i].bounding_quadrant())
     indices_tries = sorted(range(n), key=lambda k: dic_aires[k])
     inclusions = [-1] * n
     for j in range(n):
        i = j+1
        ind_j = indices_tries[j]
        while i < n :
            ind_i = indices_tries[i]
            if ind_j != ind_i and quadrant_inclus(quadrant[ind_j],quadrant[ind_i]):
                if inclusions[ind_j] == -1 or dic_aires[ind_i] < dic_aires[inclusions[ind_j]]:
                    if is_inside(polygones[ind_j].points[0],polygones[ind_i]):
                        inclusions[ind_j] = ind_i
            i+=1
     return inclusions 



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
def retourne_temps2(polygones):
    start_time = time()
    trouve_inclusions(polygones)
    end_time = time()
    execution_time = end_time - start_time
    return execution_time

if __name__ == "__main__":
    main()