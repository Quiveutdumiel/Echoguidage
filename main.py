# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:31:46 2017

@author: Echoguidage
"""
from math import atan, cos, sin, sqrt, pi, radians, tan
import serial
import time
from threading import Timer
import sys
from PyQt4 import QtGui, QtCore
from interface_simu import Ui_simu
from interface_menu import Ui_menu_principal
import os 
import numpy as np
from mesure_dist import *
from math import atan2, cos, sin, tan, pi, radians

########### Pour la visu camera
from detection_balles import *
###############################

global pos
pos = []



class echographie:
    """ Classe definissant la sonde echographique """
    
    def __init__(self,x, y, angle_x, angle_y, angle_z):
        """
        Parametres
        ----------
        x, y,angle_x,angle_y,angle_z : float
            abscisse,ordonnee,angles d'inclinaison de la sonde selon l'axe x,y,z
        """
        self.__x = x
        self.__y = y
        self.__angle_x = angle_x
        self.__angle_y = angle_y
        self.__angle_z = angle_z
        self.longueur = 0.125 #distance entre la base de la sonde et la balle en metre
        self.largeur = 0.07 #largeur de la sonde
        
    @property
    def x(self):
        """
        x: float
            abscisse de la sonde
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
        
    @property
    def y(self):
        """
        y: float
            ordonnee de la sonde
        """
        return self.__y  
        
    @y.setter
    def y(self, y):
        self.__y = y
        
    @property
    def angle_x(self):
        """
        angle_x: float
            angle selon l'axe x
        """
        return self.__angle_x  
        
    @angle_x.setter
    def angle_x(self, angle_x):
        self.__angle_x = angle_x

    @property
    def angle_y(self):
        """
        angle_y: float
            angle selon l'axe y
        """
        return self.__angle_y  
        
    @angle_y.setter
    def angle_y(self, angle_y):
        self.__angle_y = angle_y

    @property
    def angle_z(self):
        """
        angle_z: float
            angle selon l'axe z
        """
        return self.__angle_z  
        
    @angle_z.setter
    def angle_z(self, angle_z):
        self.__angle_z = angle_z



    def correction_xsonde(self, hs = 0.08):
        """ Permet de corriger la position de la sonde en fonction de son inclinaison """
        if self.x == None:
            return None
        else:
            return self.x  - hs * cos(radians(self.angle_z))

        
    def dessinimage(self, qp):
        """
        dessine l'image echographique simulee de la sonde
        """
        #arrondir l'angle a 10 pres et prendre 20 si trop grand
        #choisir l'image avec la bonne distance 
        
        if self.x == None:
            image = QtGui.QImage("erreur_detection.jpg")
        else:    
            comp = abs(np.array(mp0deg)-self.x*100)
            indice = np.argmin(comp)
            if np.max(mp0deg)>self.x>np.min(mp0deg):
                image = QtGui.QImage(dossier+'/0deg/'+str(mp0deg[indice])+" 0 0.jpg")
                print("Image correspondante "+str(mp0deg[indice]))
            else:
                image = QtGui.QImage("hors_zone.jpg")

        qp.drawImage(QtCore.QRect(0, 0, 932, 700), image)


        
class aiguille:
    """ Classe definissant l'aiguille """
    
    def __init__(self,x, y, angle_x, angle_y, angle_z, prof, inj,inclinaison):
        """
        Parametres
        ----------
        x, y, angle_x, angle_y, angle_z, prof : float
            abscisse,ordonnee,angles d'inclinaison de l'aiguille selon l'axe x,y,z , profondeur
        inj : int
            indique la quantite de liquide anesthesiant injecte
        """
        self.__x = x
        self.__y = y
        self.__angle_x = angle_x
        self.__angle_y = angle_y
        self.__angle_z = angle_z
        self.__inclinaison = inclinaison
        self.__prof = prof
        self.__inj = inj
        self.longueur = 0.19 #distance entre la pointe de l'aiguille et la balle en metre
        self.hauteur_capteur = 90 #distance pointe-capteur infrarouge en mm
        
    @property
    def x(self):
        """
        x: float
            abscisse de l'aiguille
        """
        return self.__x
        
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        """
        y: float
            ordonnee de l'aiguille
        """
        return self.__y  
        
        
    @y.setter
    def y(self, y):
        self.__y = y
        
        
    @property
    def angle_x(self):
        """
        angle_x: float
            angle selon l'axe x
        """
        return self.__angle_x  
        
    @angle_x.setter
    def angle_x(self, angle_x):
        self.__angle_x = angle_x

    @property
    def angle_y(self):
        """
        angle_y: float
            angle selon l'axe y
        """
        return self.__angle_y  
        
    @angle_y.setter
    def angle_y(self, angle_y):
        self.__angle_y = angle_y

    @property
    def angle_z(self):
        """
        angle_z: float
            angle selon l'axe z
        """
        return self.__angle_z  
        
    @angle_z.setter
    def angle_z(self, angle_z):
        self.__angle_z = angle_z
        
        
    @property
    def prof(self):
        """
        prof: float
            profondeur d'insertion de l'aiguille
        """
        return self.__prof  
        
    @prof.setter
    def prof(self, prof):
        self.__prof = prof

    @property
    def inj(self):
        """
        inj: int
            indique la quantite de liquide anesthesiant injecte
        """
        if self.__inj > 100:
            return 100
        else:
            return self.__inj 
        
    @inj.setter
    def inj(self, inj):
        if self.__inj > 100:
            self.inj__ = 100
        else:
            self.__inj = inj

    @property
    def inclinaison(self):
        """
        inclinaison: float
            angle par rapport au plan contenant la surface du pain de gel
        """
        return self.__inclinaison 
        
    @inclinaison.setter
    def inclinaison(self, inclinaison):
        self.__inclinaison = inclinaison

    def orientation(self, sonde):
        
        """ Calcule l'orientation de l'aiguille par rapport a la sonde comme decrit dans le rapport """
        xs = sonde.x
        ys = sonde.y
        xa = self.x
        ya = self.y
        
        if ya == ys or xs == None or xa == None or ys == None or ya == None:
            return 0
        else:
            return atan2(xa-xs, ya-ys)



    def pt_ponction(self, sonde):
        
        """ Calcule les coordonnees du point de ponction de l'aiguille: point d'intersection du pain de gel avec l'aiguille
        et par la meme occasion corrige la position de l'aiguille en fonction de l'angle d'inclinaison et de son orientation"""

        xa = self.x
        ya = self.y

        phi = self.orientation(sonde)
        ####################
        print("Orientation", phi)
        ####################
        theta_aiguille = radians(self.inclinaison)
        
        xp = xa - self.longueur*cos(theta_aiguille)*sin(phi)
        yp = ya - self.longueur*cos(theta_aiguille)*cos(phi)

        #print(xp,yp)
        
        return [xp, yp]



    def pt_extremite(self,sonde):
        
        """ Retourne les coordonnees du point d'injection """
        
        ponct = self.pt_ponction(sonde)
        phi = self.orientation(sonde)
        
        theta_aiguille = radians(self.inclinaison)
        profondeur = self.prof*10**(-3) #profondeur donnee en millimetres par la carte
        
        xe = ponct[0] - profondeur * cos(theta_aiguille) * sin(phi) 
        ye = ponct[1] - profondeur * cos(theta_aiguille) * cos(phi) 
        ze = -profondeur * sin(theta_aiguille)
        
        return [xe, ye, ze]  #ye ze utiles pour l IHM


    def pt_aig(self, sonde, h):
        
        """ Retourne les coordonnees d'un point de l'aiguille situe a une profondeur h """
        
        ponct = self.pt_ponction(sonde)
        phi = self.orientation(sonde)
        
        theta_aiguille = radians(self.inclinaison)
        
        x = ponct[0] - h * cos(theta_aiguille) * sin(phi)
        y = ponct[1] - h * cos(theta_aiguille) * cos(phi)
        z = -h * sin(theta_aiguille)
        
        return x, y, z
   
    
    
    def intervalle_plan(self, sonde, z, epsilon = 0.02):
        
        """ Retourne les x pour lesquels l'aiguille est dans le plan de la sonde 
        epsilon: marge d'erreur due aux fluctuations des capteurs """
    
        theta_sonde = radians(sonde.angle_z)
        
        #Si la sonde n est pas inclinee on simplifie le probleme (ce qui evite au passage une division par 0)
        if theta_sonde > 87 and theta_sonde < 93:
            x_N = sonde.x - (sonde.longueur * sin(theta_sonde) + z*sin(self.inclinaison))/tan(theta_sonde)

        #Sinon 
        elif theta_sonde < 87:
            x_N = sonde.x - (sonde.longueur * sin(theta_sonde) + z*sin(self.inclinaison))/tan(theta_sonde)
          
        else:
            x_N = - (sonde.x - (sonde.longueur * sin(theta_sonde) + z*sin(self.inclinaison))/tan(theta_sonde))
            
        return x_N - epsilon/2, x_N + epsilon/2
    
    
    
    def dernier_pt_visible(self, sonde, epsilon = 0.02, dh = 0.05):
        """ Retourne les coordonnees du dernier point de l'aiguille situe dans le plan de la sonde (point visible) """
        #marge: pour la fluctuation des capteurs
        #dh: pas de parcourt des points de l'aiguille
        h = 0
        ya = self.y
        za = 0
        verif = True
        
        while verif == True and h < self.prof:
    
            xa, ya, za = self.pt_aig(sonde, h) #point de l'aiguille courant
            x1, x2 = self.intervalle_plan(sonde, za, epsilon)
    
            #si le point courant est dans le plan, on continue de parcourir les points jusqu'à qu'un point ne soit plus valide
            if (xa <= x2 and xa >= x1) and (ya >= -sonde.largeur/2 and ya <= sonde.largeur/2):
                h += dh
    
            else:
                verif = False
                # on sort de la boucle while est on recupere le dernier point de l'aiguille bon à afficher: xa, ya, za 
        
        return ya, za

    
#    def pt_origine(self, sonde, epsilon = 0.05):
#        
#        """ Retourne l ordonnee a l origine sur l IHM, epsilon correspond au meme epsilon que dans la fonction orientation """
#        
#        x0 = sonde.x
#        y0 = sonde.y + epsilon
#        
#        pt_ext = self.pt_extremite(sonde)
#        xe = pt_ext[0]
#        ye = pt_ext[1]
#        ze = pt_ext[2]
#        
#        theta_aiguille = radians(self.angle_z)
#        
#        F = x0**2 + y0**2 - 2*x0*xe + xe**2 - 2*y0*ye + ye**2 + ze**2
#        
#        a = cos(theta_aiguille)**2
#        b = 2 * (self.prof + sin(theta_aiguille)*ze)
#        c = self.prof**2 - F
#        
#        delta = b**2 - 4*a*c
#        
#        d = (-b + sqrt(delta)) / (2*a)
#        #d2 = (-b - sqrt(delta)) / (2*a) #d2 < 0
#        
#        #print(degrees(theta_aiguille), delta, d)
#        
#        return -d*sin(theta_aiguille)
        
    
    
    
    def dessinimage(self,qp,sonde):
        """
        dessine la partie visible de l'aiguille
        """
        if self.x == None or self.y == None or sonde.x == None or sonde.y == None:
            return
        else:
            conv_x = (730.0-205.0)/0.05 #conversion metres en pixels
            conv_y = 670.0/0.1 #conversion metres en pixels
            #x image de 205 a 730 pixels 
            #y image de 0 a 670 pixel
            
            #point d origine
            #simple pour commencer
            #if self.y < 0:
                #xo = 730
            #else:
                #xo = 205
            
            xo = 730    
            yo = 0
            
            #xo = conv_x*730+ 205 #temporaire
            #yo = -conv_y*self.pt_origine(sonde)
            

            #point extremite
            #xe = conv_x*self.dernier_pt_visible(sonde)[0] + 205
            #ye = -conv_y*self.dernier_pt_visible(sonde)[1]

            extremite = self.pt_extremite(sonde)
            
            xe = conv_x*extremite[1] + 205
            ye = -conv_y*extremite[2]
            #print(xe, ye)
            
            qp.setPen( QtGui.QPen(QtCore.Qt.gray,3 ) )
            qp.drawLine(xo, yo, xe, ye)

        
    def dessininjection(self, qp,sonde):
        """
        dessine une tache rouge au niveau du point d'injection de l'aiguille
        """
        global pos
        if self.x == None or self.y == None or sonde.x == None or sonde.y == None or self.inj == 0:
            pass
        else:
            conv_x = 70#conversion centimetre en pixels
            conv_y = 134#conversion centimetre en pixels

            extremite = self.pt_extremite(sonde)
            
            xe = conv_x*extremite[1] + 205
            ye = -conv_y*extremite[2]
            #print(xe, ye)
            
            pos.append([xe,ye])
            #print(pos)
        for x in pos:
            qp.setPen( QtGui.QPen(QtCore.Qt.red,10 ) )
            #qp.drawPoint(x[0], x[1]) 
            qp.drawPoint(400, 400) 
        
        
class MonAppli_menu(QtGui.QMainWindow):
    """
    fenetre d'affichage du menu principal
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_menu_principal()
        self.ui.setupUi(self)
        self.ui.simuler.setEnabled(False)
        self.ui.simuler.clicked.connect(self.lancer_simu)
        self.ui.quitter.clicked.connect(self.quitter)
        self.ui.charger.clicked.connect(self.charger_scene)
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("image_menu.JPG")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)
        
        
    def charger_scene(self):
        global mp0deg
        global dossier
        dossier = str(self.ui.choixscene.currentText())
        mp0deg = os.listdir(dossier+'/0deg')
        for i in range(len(mp0deg)):
            mp0deg[i] = mp0deg[i].replace(' 0 0.jpg','')
            mp0deg[i] = float(mp0deg[i]) 
        self.ui.progress.setValue(100)
        self.ui.simuler.setEnabled(True)
        
    
    def quitter(self):
        self.close()
        
    def lancer_simu(self):
        global window2
        self.close()
        window2 = MonAppli_jeu()
        window2.show()

        
class MonAppli_jeu(QtGui.QMainWindow):
    """
    fenetre d'affichage de la partie simulation
    """
    def __init__(self):
        global pos
        super().__init__()
        self.ui = Ui_simu()
        self.echogra = echographie(0,0,0,0,0)
        self.aigu = aiguille(0,0,0,0,0,0,0,0)
        self.stop = 0
        pos = []
        self.cam = cv2.VideoCapture(0)
        #self.cam = cv2.VideoCapture(1) #sur ordinateur portable pour ne pas utiliser la webcam de l'ordinateur
        self.ui.setupUi(self)
        self.ui.quitter.clicked.connect(self.quitter)
        self.ui.pause.clicked.connect(self.mettre_pause)
        self.ui.menu.clicked.connect(self.retour_menu)
        self.mise_a_jour_fenetre()
        
        
    def quitter(self):
        self.stop = 1
        self.close()
        
        
    def mettre_pause(self):
        if self.ui.pause.text() == "Pause":
            self.ui.pause.setText("Reprendre")

        else:
            self.ui.pause.setText("Pause")

        
    def retour_menu(self):
        global fichier
        global window2
        self.stop = 1
        self.close()
        window2 = MonAppli_menu()
        window2.show()
  
  
    def mise_a_jour_fenetre(self):
        """
        Met a jour l'affichage ainsi que les mesures effectuees par les capteurs
        """
        dist_sonde = None
        dist_aiguille = None
        ret, frame = self.cam.read()
        
        ######################### Visu camera
        mask_sonde0, mask_aiguille0 = traitement(frame)
        contours_sonde0, contours_aiguille0 = detect_contours(frame, mask_sonde0, mask_aiguille0)
        dist_sonde0 = dist_cam_object(frame, contours_sonde0, 0, "sonde")
        dist_aig = dist_cam_object(frame, contours_aiguille0, 0, "aiguille")
        cv2.imshow('frame', frame)
        ###########################


        if ret:
            dist_sonde, dist_aiguille, ys, ya = R_3D(frame, 0)
            #x_aig, y_aig = pt_ponction(self, sonde)
        
        if self.ui.pause.text() == "Pause":
            try:
                #tri les donnees envoyees par la carte arduino
                donnees = ser.readline().decode('utf-8').strip()
                donnees = donnees[:-1]
                donnees = donnees.split(';')
            except(UnicodeDecodeError):
                print("error value")
                donnees = [0]

            erreur_type = False #
            for x in donnees:
                if not (isinstance(x, str)):
                    erreur_type = True
            
            if len(donnees) != 8 and erreur_type: #eviter bug
                pass
            else:
                donnees = [float(x) for x in donnees]#profondeur (en mm) / 0 ou 1 bouton / angle x sonde/
                #angle y sonde / angle z sonde / angle x aiguille / angle y aiguille / angle z aiguille /
                              
                self.echogra.x = dist_sonde
                self.echogra.x = self.echogra.correction_xsonde()
                if self.echogra.x != None: 
                    self.echogra.x = (self.echogra.x - 0.60) /4 #position origine en metre    
                
                self.echogra.angle_x = donnees[3]+75
                self.echogra.angle_y = donnees[4]+75
                self.echogra.angle_z = donnees[5]+75
                
                self.aigu.x = self.echogra.x
                self.aigu.y = ya
                
                self.aigu.angle_x = donnees[0]-45
                self.aigu.angle_y = donnees[1]-45
                self.aigu.angle_z = donnees[2]-45
                self.aigu.inclinaison = atan2(self.aigu.angle_y, self.aigu.angle_z)*57.3 - 10
                self.aigu.prof = self.aigu.hauteur_capteur - donnees[6] #en mm
                #self.aigu.prof = 20
                
                self.aigu.inj = donnees[7]
                
                self.ui.centralwidget.update()
        else:
            pass
        
        if self.stop == 0:
            Timer(0.05, self.mise_a_jour_fenetre).start()
        else:
            pass



    def affichage_valeurs(self):
        self.ui.label_echogra_x_name.setText("x_sonde:")
        self.ui.label_echogra_x.setText(str(self.echogra.x))
        if self.echogra.x != None:
            self.ui.label_echogra_x.setText(str(round(self.echogra.x*100,2))+"cm")
            
        self.ui.label_echogra_y_name.setText("y_sonde:")
        self.ui.label_echogra_y.setText(str(self.echogra.y))
        
        self.ui.label_echogra_angle_name.setText("inclinaison_sonde:")
        self.ui.label_echogra_angle.setText(str(round(self.echogra.angle_z,2))+"°")

        self.ui.label_aigu_x_name.setText("x_aiguille:")
        self.ui.label_aigu_x.setText(str(self.aigu.x))
        if self.aigu.x != None:
            self.ui.label_aigu_x.setText(str(round(self.aigu.x*100,2))+"cm")
            
        self.ui.label_aigu_y_name.setText("y_aiguille:")
        self.ui.label_aigu_y.setText(str(self.aigu.y))
        if self.aigu.y != None:
            self.ui.label_aigu_y.setText(str(round(self.aigu.y*100,2))+"cm")
            
        self.ui.label_aigu_angle_name.setText("inclinaison_aiguille:")
        self.ui.label_aigu_angle.setText(str(round(self.aigu.inclinaison,2))+"°")
        
        self.ui.label_aigu_prof_name.setText("profondeur_aiguille:")
        self.ui.label_aigu_prof.setText(str(self.aigu.prof)+"mm")
        
        self.ui.label_aigu_inj_name.setText("injection_aiguille:")
        self.ui.label_aigu_inj.setText(str(self.aigu.inj))

        
    def paintEvent(self, e):
        """
        Permet la mise a jour de l'affichage
        """
        qp = QtGui.QPainter()
        qp.begin(self)
        self.affichage_valeurs()
        self.drawecho(qp)
        self.drawaiguille(qp)
        self.drawinjection(qp)
        qp.end()
        

    def drawecho(self,qp):
        """
        Permet d'afficher l'image echographique
        """
        self.echogra.dessinimage(qp)
    
    def drawaiguille(self,qp):
        """
        Permet de dessiner l'aiguille
        """
        self.aigu.dessinimage(qp,self.echogra)
    
    def drawinjection(self,qp):
        """
        Permet de dessiner le point d'injection
        """
        self.aigu.dessininjection(qp,self.echogra)
        
##############################################


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #change ACM number as found from ls /dev/tty*
    #ser=serial.Serial("/dev/ttyACM0",9600) #linux
    ser=serial.Serial("\\\\.\\COM4",9600) #windows
    #ser=serial.Serial("\\\\.\\COM6",9600) #sur pc portable
    ser.baudrate=9600
    window = MonAppli_menu()
    window.show()
    app.exec_()
