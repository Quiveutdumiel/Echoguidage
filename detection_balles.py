#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:32:27 2018

@author: corazzal
"""

import cv2
from calibration_couleur import colorLower_sonde, colorUpper_sonde, colorLower_aiguille, colorUpper_aiguille

global distance_connue, diametre_connu

diametre_connu = 0.04
distance_connue = 0.3



def traitement(frame):
    
    """ Applique un changement de la bande de couleur et une ouverture pour ameliorer la detection de contours"""
    
    global colorLower_sonde, colorUpper_sonde, colorLower_aiguille, colorUpper_aiguille
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask_sonde = cv2.inRange(hsv, colorLower_sonde, colorUpper_sonde)
    mask_sonde = cv2.erode(mask_sonde, None, iterations=2)
    mask_sonde = cv2.dilate(mask_sonde, None, iterations=2)
        
    mask_aiguille = cv2.inRange(hsv, colorLower_aiguille, colorUpper_aiguille)
    mask_aiguille = cv2.erode(mask_aiguille, None, iterations=2)
    mask_aiguille = cv2.dilate(mask_aiguille, None, iterations=2)
    
    return mask_sonde, mask_aiguille




def detect_contours(frame, mask_sonde, mask_aiguille):
    
    """ Detecte et trace les contours """
    
    im,contours_aiguille, hierarchy = cv2.findContours(mask_aiguille,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im,contours_sonde, hierarchy = cv2.findContours(mask_sonde,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours_aiguille, -1, (0,0,255), 3)
    cv2.drawContours(frame, contours_sonde, -1, (0,255,0), 3)
    
    return contours_sonde, contours_aiguille




def dist_cam_object(frame, contours, n_cam, objet, F=795):
    
    """ Selectionne le contour le plus grand et l associe a un cercle d un certain rayon puis calcule la distance"""
    
    global diametre_connu
    
    dist = None
    
    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(frame,center,radius,(0,255,0),2)
        
        #Calcule de la distance camera-aiguille
        dist = diametre_connu * F / (2*radius)
        #print("distance camera n_{} - ".format(n_cam) + objet + "= {} m\n".format(dist))
        
        
    return dist



if __name__ == '__main__':
        
    cam0 = cv2.VideoCapture(0)
    
    
    while(True):
    
        #Lecture image par image
        ret0, frame0 = cam0.read()


        if ret0:
            #Camera 0
            mask_sonde0, mask_aiguille0 = traitement(frame0)
            contours_sonde0, contours_aiguille0 = detect_contours(frame0, mask_sonde0, mask_aiguille0)
            dist_sonde0 = dist_cam_object(frame0, contours_sonde0, 0, "sonde")
            dist_aig = dist_cam_object(frame0, contours_aiguille0, 0, "aiguille")


        #Affichage
        if ret0:
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
