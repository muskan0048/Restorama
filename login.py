# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
import os
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
        global a,b,e
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 81, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 75, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 68, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 110, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        a=self.lineEdit
        b=self.lineEdit_2
        e=self.label_2
        self.pushButton.clicked.connect(ob.abc)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Username", None))
        self.label_3.setText(_translate("Dialog", "Password", None))
        self.pushButton.setText(_translate("Dialog", "Log in", None))

   
    def abc(self):
        global c,d
        c= a.text()
        d=b.text()

        db = MySQLdb.connect("localhost","root","root","project" )


        cursor = db.cursor()

        sql = "SELECT * FROM login WHERE username='%s' AND password= '%s'" % (c, d) 
        print ("a")
        try:

           cursor.execute(sql)
           print("b")
           results = cursor.fetchall()
           print("c")
           for row in results:
            
            print(row)
            os.system("python3 f4.py")
           print ("success")
          
     
        except:
           print ("error")
   
        db.close()


if __name__ == "__main__":
    ob=Ui_Dialog()
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

