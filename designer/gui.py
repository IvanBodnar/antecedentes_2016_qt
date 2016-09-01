# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/gui.ui'
#
# Created: Wed Aug 31 19:43:29 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(593, 310)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.coordenadas_lineEdit = QtGui.QLineEdit(self.frame)
        self.coordenadas_lineEdit.setInputMask(_fromUtf8(""))
        self.coordenadas_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.coordenadas_lineEdit.setObjectName(_fromUtf8("coordenadas_lineEdit"))
        self.gridLayout.addWidget(self.coordenadas_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.distancia_spinBox = QtGui.QSpinBox(self.frame)
        self.distancia_spinBox.setMinimum(1)
        self.distancia_spinBox.setMaximum(10000)
        self.distancia_spinBox.setObjectName(_fromUtf8("distancia_spinBox"))
        self.gridLayout.addWidget(self.distancia_spinBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.file_toolButton = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_toolButton.sizePolicy().hasHeightForWidth())
        self.file_toolButton.setSizePolicy(sizePolicy)
        self.file_toolButton.setObjectName(_fromUtf8("file_toolButton"))
        self.gridLayout.addWidget(self.file_toolButton, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancelar_pushButton = QtGui.QPushButton(self.frame)
        self.cancelar_pushButton.setObjectName(_fromUtf8("cancelar_pushButton"))
        self.horizontalLayout.addWidget(self.cancelar_pushButton)
        self.aceptar_pushButton = QtGui.QPushButton(self.frame)
        self.aceptar_pushButton.setObjectName(_fromUtf8("aceptar_pushButton"))
        self.horizontalLayout.addWidget(self.aceptar_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Coordenadas:", None))
        self.label_2.setText(_translate("Dialog", "Distancia:", None))
        self.label_3.setText(_translate("Dialog", "Archivo de Salida:", None))
        self.file_toolButton.setText(_translate("Dialog", "...", None))
        self.cancelar_pushButton.setText(_translate("Dialog", "Cancelar", None))
        self.aceptar_pushButton.setText(_translate("Dialog", "Aceptar", None))

