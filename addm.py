# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        global a,b
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(107, 100, 111, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(110, 150, 117, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 180, 117, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        a=self.radioButton
        b=self.radioButton_2
        self.pushButton.clicked.connect(ob1.a)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter amount", None))
        self.label.setText(_translate("Dialog", "Choose Wallet:", None))
        self.radioButton.setText(_translate("Dialog", "Paytm", None))
        self.radioButton_2.setText(_translate("Dialog", "MobiKwik", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))


    def a(self):  
        if a.isChecked()==True:
            webbrowser.open('http://paytm.com')
            
        if b.isChecked()==True:
           webbrowser.open('http://mobikwik.com') 
            

if __name__ == "__main__":
    ob1=Ui_Dialog() 
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

