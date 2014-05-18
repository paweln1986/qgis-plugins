# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_graniczniki.ui'
#
# Created: Sat May 17 12:49:28 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Graniczniki(object):
    def setupUi(self, Graniczniki):
        Graniczniki.setObjectName(_fromUtf8("Graniczniki"))
        Graniczniki.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Graniczniki)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.loadButton = QtGui.QPushButton(Graniczniki)
        self.loadButton.setGeometry(QtCore.QRect(20, 240, 99, 27))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.textEdit = QtGui.QTextEdit(Graniczniki)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 381, 201))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Graniczniki)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Graniczniki.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Graniczniki.reject)
        QtCore.QMetaObject.connectSlotsByName(Graniczniki)

    def retranslateUi(self, Graniczniki):
        Graniczniki.setWindowTitle(_translate("Graniczniki", "Graniczniki", None))
        self.loadButton.setText(_translate("Graniczniki", "Load", None))

