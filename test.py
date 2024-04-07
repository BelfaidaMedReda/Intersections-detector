#!/usr/bin/env python3
import matplotlib.pyplot as plt
from main_naif import retourne_temps_naif
from main2 import retourne_temps2
from main import retourne_temps
from geo.segment import Segment
from geo.polygon import Polygon
from geo.point import Point



def carres_imbriques(width,height,n):
    polygones =[]
    gap_height = height/(2*n)
    gap_width = width /(2*n)
    for i in range(n):
        poly =[Point([i*gap_width,i*gap_height]) , Point([width-i*gap_width,i*gap_height]),Point([width-i*gap_width,height-i*gap_height]),Point([i*gap_width,height-i*gap_height])]
        polygones.append(Polygon(poly))
    return polygones

temps = []
temps2= []
temps_naif=[]
nb_poly = []

def carres_alignes(n, taille_initiale, increment):
    """
    Génère une liste de carrés alignés sans intersection, avec des côtés de longueur croissante.
   
    :param n: Nombre de carrés à générer.
    :param taille_initiale: Longueur du côté du premier carré.
    :param increment: Valeur d'augmentation de la taille des côtés à chaque nouveau carré.
    :return: Liste de polygones représentant les carrés.
    """
    polygones = []
    # Position initiale du premier carré
    x, y = 0, 0

    for i in range(n):
        taille_cote = taille_initiale + i * increment
        # Coins du carré courant
        poly = [
            Point([x, y]),  # Coin inférieur gauche
            Point([x + taille_cote, y]),  # Coin inférieur droit
            Point([x + taille_cote, y + taille_cote]),  # Coin supérieur droit
            Point([x, y + taille_cote]) # Coin supérieur gauche
        ]
        polygones.append(Polygon(poly))
       
        # Mise à jour de la position pour le prochain carré
        x += taille_cote
        y += taille_cote

    return polygones
for i in range(1000,10000,1000):
    nb_poly.append(i)
    temps2.append(retourne_temps2(carres_alignes(i,50,10)))
    temps.append(retourne_temps(carres_alignes(i,50,10)))
    temps_naif.append(retourne_temps_naif(carres_alignes(i,50,10)))

plt.plot(nb_poly,temps2,'r',label="algo3")
plt.plot(nb_poly,temps,'b',label="algo2")
plt.plot(nb_poly,temps_naif,'g',label="algo naif")
plt.grid()
plt.show()
