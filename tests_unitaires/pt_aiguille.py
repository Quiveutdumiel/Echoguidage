#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:41:15 2018

@author: corazzal
"""

from math import atan2, cos, sin, tan, pi, radians

global h_aiguille
h_aiguille = 0.12 #distance extremite-boule de marquage de l'aiguille

def orientation(sonde, aiguille):
    
    """ Calcule l'orientation de l'aiguille par rapport a la sonde comme decrit dans le rapport 
    sonde et aiguille sont les coordonnees x,y"""

    return atan2((aiguille[0] - sonde[0]), (aiguille[1] - sonde[1])) #atan2(y, x) retourne atan(y/x) en tenant compte des signes


def pt_ponction(sonde, aiguille, theta_aiguille):
    
    """ Calcule les coordonnees du point de ponction de l'aiguille: point d'intersection du pain de gel avec l'aiguille
    et par la meme occasion corrige la position de l'aiguille en fonction de l'angle d'inclinaison et de son orientation"""
    
    phi = orientation(sonde, aiguille)
    
    xp = aiguille[0] - h_aiguille*cos(radians(theta_aiguille))*sin(phi)
    yp = aiguille[1] - h_aiguille*cos(radians(theta_aiguille))*cos(phi)
    
    return xp, yp



def pt_extremite(sonde, aiguille, profondeur, theta_aiguille):

    """ Calcule les coordonnees du point ou le produit anesthesiant sera injecte """
    
    phi = orientation(sonde, aiguille)
    
    xp, yp = pt_ponction(sonde, aiguille, theta_aiguille)
    
    xe = profondeur*cos(radians(theta_aiguille))*sin(phi) + xp
    ye = -profondeur*cos(radians(theta_aiguille))*cos(phi) + yp

    ze = -profondeur*sin(radians(theta_aiguille))

    return xe, ye, ze

#    
#def intervalle_plan(sonde, aiguille, theta_aiguille, z, epsilon = 0.1):
#        
#    """ Retourne les y pour lesquels l'aiguille est dans le plan de la sonde """
#
#    theta_sonde = radians(sonde.angle_z)
#
#    yp = sonde.y + sonde.longueur*cos(theta_sonde)
#    
#    #pour eviter une division par 0
#    if theta_sonde >= -5 and theta_sonde <= 5:
#        y1 = yp - epsilon
#        
#    else:
#        y1 = yp - epsilon + (z/tan(theta_sonde))
#
#    return y1, y1 + 2*epsilon
#    
#
#
#def dernier_pt_visible(sonde, aiguille, theta_aiguille, marge = 0.05, dh = 0.05):
#    """ Retourne les coordonnees du dernier point de l'aiguille situe dans le plan de la sonde (point visible) """
#    #marge: pour la fluctuation des capteurs
#    #dh: pas de parcourt des points de l'aiguille
#        
#    h = 0
#    ya = aiguille[1]
#    za = 0
#    verif = True
#    
#    profondeur = 0.1
#        
#    while verif == True and h < profondeur:
#    
#        xa, ya, za = pt_extremite(sonde, aiguille, h, theta_aiguille) #point de l'aiguille courant
#        y1,y2 = intervalle_plan(sonde, aiguille, theta_aiguille, z, epsilon = 0.1)
#    
#        if (ya <= y2 and ya >= y1) and (xa >= sonde.x - marge and xa <= sonde.x + marge):
#            h += dh
#    
#        else:
#            verif = False
#            # on sort de la boucle est on recupere le dernier point de l'aiguille bon à afficher: xa, ya, za 
#        
#    return ya, za
    
if __name__ == "__main__":
    
    sonde = [0, 0]
    aiguille = [0.1, 0.1]
    profondeur = 2
    theta_aiguille = 45
    
    print(pt_extremite(sonde, aiguille, profondeur, theta_aiguille))
    
    pt_extremite(sonde, aiguille, profondeur, theta_aiguille)
