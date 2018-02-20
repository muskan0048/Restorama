# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f5.ui'
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
        global a,b,c,d,e,f,g,h
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 466)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 141, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 110, 111, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 170, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 170, 113, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 270, 191, 78))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))        
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 390, 113, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 390, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 220, 113, 27))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(240, 220, 113, 27))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 300,90, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 250, 50))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        a=self.lineEdit
        b=self.lineEdit_2
        c=self.lineEdit_3
        d=self.lineEdit_4
        e=self.lineEdit_6
        f=self.lineEdit_7
        g=self.lineEdit_8
        h=self.lineEdit_5
        self.pushButton.clicked.connect(ob.abc)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", " Restaurant Name", None))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Avg Cost for 2", None))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Email address", None))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Phone No", None))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "City", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "Cuisines", None))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog", "Type", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address:</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#55aaff;\">Register Here!</span></p></body></html>", None))


    def abc(self):
        
        v1 = a.text()
        v2 = int(b.text())
        
        v4 = d.text()
        v5 = e.text()
        v6 = f.text()
        v7 = g.text()
        v8 = h.text()
        
        db = MySQLdb.connect("localhost","root","root","project" )
      
        try:
            cursor = db.cursor()

            sql = "Insert into resto values(3, '%s', %d, '%s', '%s', '%s', '%s', '%s')" % (v1, v2, v4, v5, v6, v7, v8)
            cursor.execute(sql)
            db.commit()
        except:
            print ("Error")
        
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

