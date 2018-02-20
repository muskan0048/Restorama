# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f2.ui'
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
        global a, b, r
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 510)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 170, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 141, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 240, 380, 200))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 450, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 120, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        a=self.lineEdit
        b=self.lineEdit_2
        r=self.textEdit
        self.pushButton.clicked.connect(ob.abc)
        self.pushButton_2.clicked.connect(ob1.ab)
        self.pushButton_3.clicked.connect(ob2.ac)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Search", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Your City", None))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter Your Budget", None))
        self.pushButton_2.setText(_translate("Dialog", "Book", None))
        self.pushButton_3.setText(_translate("Dialog", "New User?", None))


    def abc(self):
        global c,d
        c= a.text()
        d= int(b.text())
        
        
        db = MySQLdb.connect("localhost","root","root","project" )
      

        cursor = db.cursor()

        sql = "SELECT * FROM Resto WHERE city='%s' AND avgcost > %d" % (c, d) 
      
        

        cursor.execute(sql)
         
        results = cursor.fetchall()
           
           
        for row in results:
          l=row
          myset = set()
          myset.add(row[1])
          myset.add(row[2])
          myset.add(row[3])
          myset.add(row[4])
          myset.add(row[5])
          myset.add(row[6])
          myset.add(row[7])
          print(l)
          n= ' , '.join(str(s) for s in myset)
          r.setText(n)  
           
        
        db.close()
        

    
    def ab(self):
        os.system("python3 login.py")
    def ac(self):
        os.system("python3 f5.py")





if __name__ == "__main__":
    ob=Ui_Dialog()
    ob1=Ui_Dialog()
    ob2=Ui_Dialog()
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

