#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:32:27 2018

@author: corazzal
"""

import cv2
from numpy import arcsin, cos, radians
import time

from calibration_couleur import colorLower_sonde, colorUpper_sonde, colorLower_aiguille, colorUpper_aiguille

# Parametres pour le calcul de la distance en metre
global distance_connue, diametre_connu, zpdg, l_sonde, l_aiguille, zcam

diametre_connu = 0.04
distance_connue = 0.3
zcam = 0.165 #hauteur de la camera par rapport a la table en metre
zpdg = 0.045 #hauteur du pain de gel par rapport a la table
l_sonde = 0.125 #hauteur de la sonde
l_aiguille = 0.180 #hauteur de l aiguille

def R_3D(frame, n_cam):
    
    """ Retourne le couple distance camera-sonde, distance camera-aiguille et le couple xs, xa en pixels"""
    
    global colorLower_sonde, colorUpper_sonde, colorLower_aiguille, colorUpper_aiguille, diametre_connu
    
# =============================================================================
#   Prétraitement d image
# =============================================================================

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask_sonde = cv2.inRange(hsv, colorLower_sonde, colorUpper_sonde)
    mask_sonde = cv2.erode(mask_sonde, None, iterations=2)
    mask_sonde = cv2.dilate(mask_sonde, None, iterations=2)
        
    mask_aiguille = cv2.inRange(hsv, colorLower_aiguille, colorUpper_aiguille)
    mask_aiguille = cv2.erode(mask_aiguille, None, iterations=2)
    mask_aiguille = cv2.dilate(mask_aiguille, None, iterations=2)
    
    
# =============================================================================
#   Contours
# =============================================================================
    im1, contours_aiguille, h1 = cv2.findContours(mask_aiguille,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im2, contours_sonde, h2 = cv2.findContours(mask_sonde,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# =============================================================================
#   Calcul de R
# =============================================================================
    
    dist_a = None
    dist_s = None
    ys = None
    ya = None
    F = 795
    Fy = 795
    
    if len(contours_sonde) > 0:
        cnt_s = max(contours_sonde, key=cv2.contourArea)
        ((ys, y), radius_s) = cv2.minEnclosingCircle(cnt_s)
        diametre_pixels_sonde = 2*int(radius_s)
        
        #Calcule de la distance camera-sonde
        dist_s = diametre_connu * F / diametre_pixels_sonde
        
    if len(contours_aiguille) > 0:
        cnt_a = max(contours_aiguille, key=cv2.contourArea)
        ((ya, y), radius_a) = cv2.minEnclosingCircle(cnt_a)
        diametre_pixels_aig = 2*int(radius_a)
        
        #Calcule de la distance camera-aiguille
        dist_a = diametre_connu * F / diametre_pixels_aig

    #Calcul de la distance entre les deux boules de marquage
    if ys != None and ya != None:
        #Constante par plan pour la conversion pixels/metres
        Fy = diametre_connu / (2*radius_s)
        ya = (ya-ys)*Fy
        ys = 0
        
    return dist_s, dist_a, ys, ya


def R_2D(z_balle,R):
    """Fonction pour se ramener a un probleme 2D"""
    if R != None:
        global zcam
        beta = arcsin((zcam - z_balle) / R)
        return R*cos(beta)
    else:
        return None


if __name__ == '__main__':
    
    cam0 = cv2.VideoCapture(0)
    
    while(True):
    
        #Lecture image par image
        ret0, frame0 = cam0.read()
        
        alpha = 0 # Angle mesure avec l accelerometre sur la sonde    
        z_balle_sonde = zpdg + cos(radians(alpha))*l_sonde
        
        theta = 45 #Angle mesure avec l accelerometre sur l aiguille
        z_balle_aiguille = zpdg + cos(radians(theta))*l_aiguille

        if ret0:
            #Camera 0
            dist_sonde0, dist_aiguille0, ys, ya = R_3D(frame0, 0)
            
            #Passage en 2D
            dist_sonde0_2D = R_2D(z_balle_sonde, dist_sonde0)
            dist_aiguille0_2D = R_2D(z_balle_aiguille, dist_aiguille0)
            
            #print("distance camera n_{} - ".format(0) + "sonde" + "= {} m\n".format(dist_sonde0_2D))
            #print("distance camera n_{} - ".format(0) + "aiguille" + "= {} m\n".format(dist_aiguille0_2D))
            #print("ys, ya =", [ys,ya])
            time.sleep(0.1)

            # Affichage des images
            cv2.imshow('frame0', frame0)
            key = cv2.waitKey(1)
            if  key == ord('q'):
                 break
        else:
            break
      
      
    # Fermeture lorsque la touche 'q' est appuyee
    cam0.release()
    cv2.destroyAllWindows()
