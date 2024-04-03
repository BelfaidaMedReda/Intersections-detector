#!/usr/bin/env python3
"""
fichier principal pour la detection des inclusions.
ce fichier est utilise pour les tests automatiques.
attention donc lors des modifications.
"""
import sys
from tycat import read_instance

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
             if (x < x1 + (x1-x2)*(y-y1)/(y1-y2) :
                 cont += 1
     return cont%2 == 1
 
def est_inclu(poly1,poly2):
     point = poly1.points[0]
     return is_inside(point,poly2)

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
     inclusions = []
     quadrant = []
     quadrants = [poly.bounding_quadrant() for poly in polygones]
     indices_tries = sorted(range(n), key=lambda k: quadrant[k].max_coordinates[0])
     inclusions = [-1] * n
     for j in range(n):
         i = j+1
         ind_j = indices_tries[j]
         while i < n :
             ind_i = indices_tries[i]
             if quadrant_inclus(quadrant[ind_j],quadrant[ind_i]):
                 if est_inclu(polygones[ind_j],polygones[ind_i]):
                     inclusions[ind_j] = ind_i
                     break
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
    

if __name__ == "__main__":
    main()
