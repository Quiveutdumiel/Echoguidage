#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:37:42 2018

@author: corazzal
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Corazza
"""

import unittest
from pt_aiguille import *

class TestCases(unittest.TestCase):
    
    def test_orientation(self):
        
        #On teste les 4 cadrans et le cas x_sonde = x_aiguille
        #les tests sont justes, il faut bien comprendre que le repere du cercle trigo et le repere de l'aiguille sont inverses
        
        sonde = [0, 0]
        aiguille = [0, 1]
        phi = orientation(sonde, aiguille)
        self.assertEqual(round(phi, 5), 0) #on tronque pour eviter une erreur de test due aux arrondis de python
        
        sonde = [0, 0]
        aiguille = [cos(pi/4), sin(pi/4)]
        phi = orientation(sonde, aiguille)
        self.assertEqual(round(phi, 5), round(pi/4, 5)) #on tronque pour eviter une erreur de test due aux arrondis de python
             
        sonde = [0, 0]
        aiguille = [-cos(pi/4), sin(pi/4)]
        phi = orientation(sonde, aiguille)
        self.assertEqual(round(phi, 5), round(-pi/4, 5))
        
        sonde = [0, 0]
        aiguille = [cos(pi/4), -sin(pi/4)]
        phi = orientation(sonde, aiguille)
        self.assertEqual(round(phi, 5), round(3*pi/4, 5))
        
        sonde = [0, 0]
        aiguille = [-cos(pi/4), -sin(pi/4)]
        phi = orientation(sonde, aiguille)
        self.assertEqual(round(phi, 5), round(-3*pi/4, 5))
        
        
    
    def test_pt_ponction(self):
        
        sonde = [0, 0]
        aiguille = [cos(pi/4), sin(pi/4)]
        theta_aiguille = 45
        xp, yp = pt_ponction(sonde, aiguille, theta_aiguille)
        
        sonde = [cos(pi/4), sin(pi/4)]
        aiguille = sonde
        theta_aiguille = 45
        xp, yp = pt_ponction(sonde, aiguille, theta_aiguille)
        self.assertEqual(xp, aiguille[0])
        
        sonde = [0, 0]
        aiguille = [sin(pi/2), 0]
        theta_aiguille = 45
        xp, yp = pt_ponction(sonde, aiguille, theta_aiguille)
        if yp < 1e-15: yp = 0 #python approxime le 0 en un flottant tres petit
        self.assertEqual(yp, aiguille[1])
        
#        
#    def test_pt_extremite(self):
#        
#        sonde = [0, 0]
#        aiguille = [cos(pi/4), sin(pi/4)]
#        profondeur = 0.1
#        theta_aiguille = 45
#        xe, ye, ze = pt_extremite(sonde, aiguille, profondeur, theta_aiguille)
#        self.assertEqual(round(xe, 3), 0.697)
#        self.assertEqual(round(ye, 3), 0.697)
#        self.assertEqual(round(ze, 3), -0.071)
        

        

if __name__ == '__main__':
    unittest.main()
