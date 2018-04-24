# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projet_python_V2\ihm_menu_robot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_simu(object):
    def setupUi(self, menu_principal):
        menu_principal.setObjectName(_fromUtf8("menu_principal"))
        menu_principal.resize(932, 700)
        self.centralwidget = QtGui.QWidget(menu_principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.menu = QtGui.QPushButton(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(700, 620, 75, 23))
        self.menu.setObjectName(_fromUtf8("pushButton_menu"))


        self.label_echogra_x_name = QtGui.QLabel(self.centralwidget)
        self.label_echogra_x_name.setGeometry(QtCore.QRect(730, 20, 151, 20))
        self.label_echogra_x_name.setObjectName(_fromUtf8("label_echogra_x_name"))
        self.label_echogra_x = QtGui.QLabel(self.centralwidget)
        self.label_echogra_x.setGeometry(QtCore.QRect(730, 50, 151, 20))
        self.label_echogra_x.setObjectName(_fromUtf8("label_echogra_x"))

        self.label_echogra_y_name = QtGui.QLabel(self.centralwidget)
        self.label_echogra_y_name.setGeometry(QtCore.QRect(730, 90, 151, 20))
        self.label_echogra_y_name.setObjectName(_fromUtf8("label_echogra_y_name"))
        self.label_echogra_y = QtGui.QLabel(self.centralwidget)
        self.label_echogra_y.setGeometry(QtCore.QRect(730, 120, 151, 20))
        self.label_echogra_y.setObjectName(_fromUtf8("label_echogra_y"))
        
        self.label_echogra_angle_name = QtGui.QLabel(self.centralwidget)
        self.label_echogra_angle_name.setGeometry(QtCore.QRect(730, 160, 151, 20))
        self.label_echogra_angle_name.setObjectName(_fromUtf8("label_echogra_angle_name"))
        self.label_echogra_angle = QtGui.QLabel(self.centralwidget)
        self.label_echogra_angle.setGeometry(QtCore.QRect(730, 190, 151, 20))
        self.label_echogra_angle.setObjectName(_fromUtf8("label_echogra_angle"))

        self.label_aigu_x_name = QtGui.QLabel(self.centralwidget)
        self.label_aigu_x_name.setGeometry(QtCore.QRect(730, 230, 151, 20))
        self.label_aigu_x_name.setObjectName(_fromUtf8("label_aigu_x_name"))
        self.label_aigu_x = QtGui.QLabel(self.centralwidget)
        self.label_aigu_x.setGeometry(QtCore.QRect(730, 260, 151, 20))
        self.label_aigu_x.setObjectName(_fromUtf8("label_aigu_x"))

        self.label_aigu_y_name = QtGui.QLabel(self.centralwidget)
        self.label_aigu_y_name.setGeometry(QtCore.QRect(730, 300, 151, 20))
        self.label_aigu_y_name.setObjectName(_fromUtf8("label_aigu_y_name"))
        self.label_aigu_y = QtGui.QLabel(self.centralwidget)
        self.label_aigu_y.setGeometry(QtCore.QRect(730, 330, 151, 20))
        self.label_aigu_y.setObjectName(_fromUtf8("label_aigu_y"))

        self.label_aigu_angle_name = QtGui.QLabel(self.centralwidget)
        self.label_aigu_angle_name.setGeometry(QtCore.QRect(730, 370, 151, 20))
        self.label_aigu_angle_name.setObjectName(_fromUtf8("label_aigu_angle_name"))
        self.label_aigu_angle = QtGui.QLabel(self.centralwidget)
        self.label_aigu_angle.setGeometry(QtCore.QRect(730, 410, 151, 20))
        self.label_aigu_angle.setObjectName(_fromUtf8("label_aigu_angle"))

        self.label_aigu_prof_name = QtGui.QLabel(self.centralwidget)
        self.label_aigu_prof_name.setGeometry(QtCore.QRect(730, 450, 151, 20))
        self.label_aigu_prof_name.setObjectName(_fromUtf8("label_aigu_prof_name"))
        self.label_aigu_prof = QtGui.QLabel(self.centralwidget)
        self.label_aigu_prof.setGeometry(QtCore.QRect(730, 470, 151, 20))
        self.label_aigu_prof.setObjectName(_fromUtf8("label_aigu_prof"))

        self.label_aigu_inj_name = QtGui.QLabel(self.centralwidget)
        self.label_aigu_inj_name.setGeometry(QtCore.QRect(730, 510, 151, 20))
        self.label_aigu_inj_name.setObjectName(_fromUtf8("label_aigu_inj_name"))
        self.label_aigu_inj = QtGui.QLabel(self.centralwidget)
        self.label_aigu_inj.setGeometry(QtCore.QRect(730, 540, 151, 20))
        self.label_aigu_inj.setObjectName(_fromUtf8("label_aigu_inj"))
        

        self.quitter = QtGui.QPushButton(self.centralwidget)
        self.quitter.setGeometry(QtCore.QRect(810, 620, 75, 23))
        self.quitter.setObjectName(_fromUtf8("pushButton_quitter"))
        self.pause = QtGui.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(80, 620, 90, 23))
        self.pause.setObjectName(_fromUtf8("pushButton_pause"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 400, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.layout_menu = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_menu.setObjectName(_fromUtf8("layout_menu"))
        self.fond = QtGui.QWidget(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.fond.setObjectName(_fromUtf8("fond"))
        self.fond.raise_()
        self.menu.raise_()
        self.quitter.raise_()
        self.pause.raise_()
        self.horizontalLayoutWidget.raise_()
        menu_principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(menu_principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        menu_principal.setStatusBar(self.statusbar)
        self.actionQuitter = QtGui.QAction(menu_principal)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))

        self.retranslateUi(menu_principal)
        QtCore.QMetaObject.connectSlotsByName(menu_principal)

    def retranslateUi(self, menu_principal):
        menu_principal.setWindowTitle(_translate("menu_principal", "Simulation", None))
        self.menu.setText(_translate("menu_principal", "Menu", None))
        self.quitter.setText(_translate("menu_principal", "Quitter", None))

        self.label_echogra_x_name.setStyleSheet("#label_echogra_x_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_echogra_x.setStyleSheet("#label_echogra_x { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_echogra_y_name.setStyleSheet("#label_echogra_y_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_echogra_y.setStyleSheet("#label_echogra_y { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_echogra_angle_name.setStyleSheet("#label_echogra_angle_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_echogra_angle.setStyleSheet("#label_echogra_angle { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_aigu_x_name.setStyleSheet("#label_aigu_x_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_aigu_x.setStyleSheet("#label_aigu_x { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_aigu_y_name.setStyleSheet("#label_aigu_y_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_aigu_y.setStyleSheet("#label_aigu_y { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_aigu_angle_name.setStyleSheet("#label_aigu_angle_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_aigu_angle.setStyleSheet("#label_aigu_angle { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_aigu_prof_name.setStyleSheet("#label_aigu_prof_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_aigu_prof.setStyleSheet("#label_aigu_prof { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

        self.label_aigu_inj_name.setStyleSheet("#label_aigu_inj_name { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")
        self.label_aigu_inj.setStyleSheet("#label_aigu_inj { background-color: transparent; color: white; font-size: "+str(int(20))+"px;}")

                
        self.pause.setText(_translate("menu_principal", "Pause", None))
        self.actionQuitter.setText(_translate("menu_principal", "Quitter", None))
        self.actionQuitter.setShortcut(_translate("menu_principal", "Ctrl+Q", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    simu = QtGui.QMainWindow()
    ui = Ui_simu()
    ui.setupUi(simu)
    simu.show()
    sys.exit(app.exec_())

