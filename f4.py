# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import MySQLdb

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
        global a,b,c,g,date,time
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(102, 30, 181, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(27, 90, 141, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(200, 80, 110, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(27, 130, 141, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.timeEdit = QtGui.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(200, 120, 118, 27))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton2 = QtGui.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(130, 190, 99, 27))
        self.pushButton2.setObjectName(_fromUtf8("pushButton"))

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 220, 113, 27))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        g=self.lineEdit_2
        self.pushButton.clicked.connect(ob.abc)
        self.pushButton2.clicked.connect(ob.abcd)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        a=self.lineEdit

        b=self.dateEdit.text()

        c=self.timeEdit.text()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Restaurant Name", None))
        self.label.setText(_translate("Dialog", "Enter Booking Date", None))
        self.label_2.setText(_translate("Dialog", "Enter Booking Time", None))
        self.pushButton.setText(_translate("Dialog", "Book", None))
        self.pushButton2.setText(_translate("Dialog", "Offers", None))
        self.label_3.setText(_translate("Dialog", "Booking Status:", None))


    def abc(self):
            global d,e,f
            d = a.text()
            e = b
            f = c

            db = MySQLdb.connect("localhost", "root", "root", "project")

        
            cursor = db.cursor()
            sql = "select * from booking "
            cursor.execute(sql)
            results = cursor.fetchall()
            t=0
            if (cursor.rowcount == 0 ):
                print("first")
                g.setText("Reserved")
                sql1 = "Insert into booking values('%s', '%s', '%s')" % (d, e, f)
                cursor.execute(sql1)
                db.commit()


            else :
                for row in results:

                    if (d==row[0] and e==row[1] and f==row[2]):
                        t=1

                if t==1:
                    print('no')
                    g.setText("Waiting")


                else:
                    print('yes')
                    g.setText("Reserved")
                    sql1 = "Insert into booking values('%s', '%s', '%s')" % (d, e, f)
                    cursor.execute(sql1)
                    db.commit()



        

            db.close()

    def abcd(self):
        os.system("python3 f6.py")



if __name__ == "__main__":
    ob=Ui_Dialog()
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

