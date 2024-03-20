#!/usr/bin/env python3
"""
fichier principal pour la detection des inclusions.
ce fichier est utilise pour les tests automatiques.
attention donc lors des modifications.
"""
import sys
from tycat import read_instance


def is_inside(Point,polygone):
    """
    Implémentation du ray casting algorithm en python !
    """
    xp=Point.coordinates[0]
    yp=Point.coordinates[1]
    intersections=0
    segments=polygone.segments()
    for edge in segments:
        first_point=edge.endpoints[0]
        second_point=edge.endpoints[1]
        x1=first_point.coordinates[0]
        y1=first_point.coordinates[1]
        x2=second_point.coordinates[0]
        y2=second_point.coordinates[1]
        try:
            x0=x2+(x2-x1)*(yp-y2)/(y2-y1)
            if (yp<y1)!=(yp<y2) and xp<x0:
                intersections+=1
        except ZeroDivisionError:
            continue
    return intersections%2==1

def trouve_inclusions(polygones):
    """
    renvoie le vecteur des inclusions
    la ieme case contient l'indice du polygone
    contenant le ieme polygone (-1 si aucun).
    (voir le sujet pour plus d'info)
    """
    polygones_number = len(polygones)
    inclusions_liste = [-1] * polygones_number

    for i in range(polygones_number):
        point_ref = polygones[i].points[0]  # Choisissez un point de référence dans le polygone i
        reste_polygones = [(j,polygones[j]) for j in range(polygones_number) if j != i]

        for j, poly in reste_polygones:
            if is_inside(point_ref, poly):
                inclusions_liste[i] = j
                break  # Une fois qu'on a trouvé l'inclusion, on peut passer au polygone suivant
            else:
                continue

    return inclusions_liste


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
