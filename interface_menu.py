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

class Ui_menu_principal(object):
    def setupUi(self, menu_principal):
        menu_principal.setObjectName(_fromUtf8("menu_principal"))
        menu_principal.resize(800, 600)
        self.centralwidget = QtGui.QWidget(menu_principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.simuler = QtGui.QPushButton(self.centralwidget)
        self.simuler.setGeometry(QtCore.QRect(620, 220, 141, 61))
        self.simuler.setObjectName(_fromUtf8("pushButton_simu"))
        self.quitter = QtGui.QPushButton(self.centralwidget)
        self.quitter.setGeometry(QtCore.QRect(650, 430, 81, 31))
        self.quitter.setObjectName(_fromUtf8("pushButton_quitter"))
        self.charger = QtGui.QPushButton(self.centralwidget)
        self.charger.setGeometry(QtCore.QRect(610, 520, 181, 40))
        self.charger.setObjectName(_fromUtf8("pushButton_charger"))
        self.progress = QtGui.QProgressBar(self.centralwidget)
        self.progress.setObjectName(_fromUtf8("Progressbar"))
        self.progress.setGeometry(620,160,151,21)
        self.progress.setValue(0)
        self.label_charge = QtGui.QLabel(self.centralwidget)
        self.label_charge.setGeometry(QtCore.QRect(620, 130, 151, 20))
        self.label_charge.setObjectName(_fromUtf8("label_charge"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 400, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.layout_menu = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_menu.setObjectName(_fromUtf8("layout_menu"))
        self.choixscene = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.choixscene.setObjectName(_fromUtf8("choixscene"))
        self.choixscene.addItem(_fromUtf8(""))
        self.choixscene.addItem(_fromUtf8(""))
        self.choixscene.addItem(_fromUtf8(""))
        self.choixscene.addItem(_fromUtf8(""))
        self.choixscene.addItem(_fromUtf8(""))
        self.layout_menu.addWidget(self.choixscene)
        self.fond = QtGui.QWidget(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.fond.setObjectName(_fromUtf8("fond"))
        self.fond.raise_()
        self.simuler.raise_()
        self.quitter.raise_()
        self.charger.raise_()
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
        menu_principal.setWindowTitle(_translate("menu_principal", "Menu", None))
        self.simuler.setText(_translate("menu_principal", "Simulation", None))
        self.quitter.setText(_translate("menu_principal", "Quitter", None))
        self.label_charge.setText(_translate("menu_principal", "Chargement", None))
        self.charger.setText(_translate("menu_principal", "Charger le scenario", None))
        self.choixscene.setItemText(0, _translate("menu_principal", "choix du scenario", None))
        self.choixscene.setItemText(1, _translate("menu_principal", "genoux", None))
        self.choixscene.setItemText(2, _translate("menu_principal", "Nerf_femoral", None))
        self.choixscene.setItemText(3, _translate("menu_principal", "ventre", None))
        self.choixscene.setItemText(4, _translate("menu_principal", "mollet", None))
        self.actionQuitter.setText(_translate("menu_principal", "Quitter", None))
        self.actionQuitter.setShortcut(_translate("menu_principal", "Ctrl+Q", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    menu_principal = QtGui.QMainWindow()
    ui = Ui_menu_principal()
    ui.setupUi(menu_principal)
    menu_principal.show()
    sys.exit(app.exec_())

