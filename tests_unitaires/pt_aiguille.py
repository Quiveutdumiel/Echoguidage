#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:41:15 2018

@author: corazzal
"""

from math import atan2, cos, sin, tan, pi, radians, degrees

global h_aiguille, h_sonde, l_sonde
h_aiguille = 0.19 #distance extremite-boule de marquage de l'aiguille
h_sonde = 0.125
l_sonde = 0.07


def orientation(sonde, aiguille):
    
    """ Calcule l'orientation de l'aiguille par rapport a la sonde comme decrit dans le rapport 
    sonde et aiguille sont les coordonnees x,y"""

    return atan2((aiguille[0] - sonde[0]), (aiguille[1] - sonde[1])) #atan2(y, x) retourne atan(y/x) en tenant compte des signes



def pt_ponction(sonde, aiguille, theta_aiguille):
    
    """ Calcule les coordonnees du point de ponction de l'aiguille: point d'intersection du pain de gel avec l'aiguille
    et par la meme occasion corrige la position de l'aiguille en fonction de l'angle d'inclinaison et de son orientation"""
    
    phi = orientation(sonde, aiguille)
    theta_aiguille = radians(theta_aiguille)
    
    xp = aiguille[0] - h_aiguille*cos(theta_aiguille)*sin(phi)
    yp = aiguille[1] - h_aiguille*cos(theta_aiguille)*cos(phi)
    
    return xp, yp




def pt_extremite(sonde, aiguille, theta_aiguille, profondeur):

    """ Calcule les coordonnees du point ou le produit anesthesiant sera injecte """
    
    phi = orientation(sonde, aiguille)  
    xp, yp = pt_ponction(sonde, aiguille, theta_aiguille)
    theta_aiguille = radians(theta_aiguille)
    
    xe = -profondeur*cos(theta_aiguille)*sin(phi) + xp
    ye = -profondeur*cos(theta_aiguille)*cos(phi) + yp
    ze = -profondeur*sin(theta_aiguille)

    return xe, ye, ze



def pt_aig(sonde, aiguille, theta_aiguille, h):
        
    """ Retourne les coordonnees d'un point de l'aiguille situe a une profondeur h """
    
    xp, yp = pt_ponction(sonde, aiguille, theta_aiguille)
    phi = orientation(sonde, aiguille)
    
    theta_aiguille = radians(theta_aiguille)
    
    x = xp - h * cos(theta_aiguille) * sin(phi)
    y = yp - h * cos(theta_aiguille) * cos(phi)
    z = -h * sin(theta_aiguille)
    
    return x, y, z


  
def intervalle_plan(sonde, aiguille, theta_sonde, theta_aiguille, z, epsilon = 0.1):
        
    """ Retourne les x pour lesquels l'aiguille est dans le plan de la sonde """


    #Si la sonde n est pas inclinee on simplifie le probleme
    if (theta_sonde > 87 and theta_sonde < 93) or (theta_sonde == 0):
        x_N = sonde[0]

    #sinon voir details dans le rapport
    elif theta_sonde < 87:
        x_N = sonde[0] - (h_sonde * sin(radians(theta_sonde)) + z*sin(radians(theta_aiguille)))/tan(radians(theta_sonde))
      
    else:
        x_N = - (sonde[0] - (h_sonde * sin(radians(theta_sonde)) + z*sin(radians(theta_aiguille)))/tan(radians(theta_sonde)))
        
    return x_N - epsilon/2, x_N + epsilon/2
    



def dernier_pt_visible(sonde, aiguille, theta_sonde, theta_aiguille, profondeur, epsilon = 0.02, dh = 0.005):
    """ Retourne les coordonnees du dernier point de l'aiguille situe dans le plan de la sonde (point visible) """
    #marge: pour la fluctuation des capteurs
    #dh: pas de parcourt des points de l'aiguille
        
    h = 0
    ya = aiguille[1]
    verif = True
    
    while verif == True and h < profondeur:

        xa, ya, za = pt_aig(sonde, aiguille, theta_aiguille, h) #point de l'aiguille courant
        x1, x2 = intervalle_plan(sonde, aiguille, theta_sonde, theta_aiguille, h)

        #si le point courant est dans le plan, on continue de parcourir les points jusqu'à qu'un point ne soit plus valide
        if (xa <= x2 and xa >= x1) and (ya >= -l_sonde/2 and ya <= l_sonde/2):
            h += dh

        else:
            verif = False
            # on sort de la boucle while est on recupere le dernier point de l'aiguille bon à afficher: xa, ya, za 
    
    return ya, za

    

if __name__ == "__main__":
    
    sonde = [0, 0]
    aiguille = [0.1, 0.1]
    profondeur = 0.02
    theta_sonde = 90
    theta_aiguille = 45

    print(pt_ponction(sonde, aiguille, theta_aiguille))
    print(pt_extremite(sonde, aiguille, profondeur, theta_aiguille))
    print(pt_aig(sonde, aiguille, theta_aiguille, profondeur))
    print(intervalle_plan(sonde, aiguille, theta_sonde, theta_aiguille, profondeur))
    print(dernier_pt_visible(sonde, aiguille, theta_sonde, theta_aiguille, profondeur))
