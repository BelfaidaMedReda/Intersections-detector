#!/usr/bin/env python3
"""
fichier principal pour la detection des inclusions.
ce fichier est utilise pour les tests automatiques.
attention donc lors des modifications.

Ce script est le script de l'algo naïf !

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
            if (x < x1 + (x1-x2)*((y-y1)/(y1-y2)) or x < x2 + ((y -y2)/(y1-y2))*(x1-x2)):
                cont += 1
    return cont%2 == 1
 
def est_inclu(poly1,poly2):
    point = poly1.points[0]
    return is_inside(point,poly2)
 
def trouve_inclusions(polygones):
    """
    renvoie le vecteur des inclusions
    la ieme case contient l'indice du polygone
    contenant le ieme polygone (-1 si aucun).
    (voir le sujet pour plus d'info)
    """
    inclusions = []
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
        
def retourne_temps(polygones):
    start_time = time()
    trouve_inclusions(polygones)
    end_time = time()
    execution_time = end_time - start_time
    return execution_time

if __name__ == "__main__":
    main()
