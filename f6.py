# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f6.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import webbrowser
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 377)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 280, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 187, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton1 = QtGui.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(120, 290, 187, 41))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton2 = QtGui.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(120, 100, 187, 41))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton.clicked.connect(ob1.a)
        self.pushButton1.clicked.connect(ob2.b)
        self.pushButton2.clicked.connect(ob3.c)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#aa0000;\">Offers and Deals</span></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "Book a Cab Back home", None))
        self.pushButton1.setText(_translate("Dialog", "Book a Hotel Nearby", None))
        self.pushButton2.setText(_translate("Dialog", "Pay from wallet", None))

        
    def a(self):
        os.system("python3 cab.py")
        
    def b(self):
        webbrowser.open('http://oyorooms.com')


    def c(self):
        os.system("python3 wallet.py")

if __name__ == "__main__":
    ob1=Ui_Dialog() 
    ob2=Ui_Dialog()
    ob3=Ui_Dialog()
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

