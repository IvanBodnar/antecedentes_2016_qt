# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/gui.ui'
#
# Created: Fri Sep  2 15:33:41 2016
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
        Dialog.resize(637, 345)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.coordenadas_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.coordenadas_lineEdit.setInputMask(_fromUtf8(""))
        self.coordenadas_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.coordenadas_lineEdit.setObjectName(_fromUtf8("coordenadas_lineEdit"))
        self.gridLayout.addWidget(self.coordenadas_lineEdit, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.distancia_spinBox = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distancia_spinBox.sizePolicy().hasHeightForWidth())
        self.distancia_spinBox.setSizePolicy(sizePolicy)
        self.distancia_spinBox.setMinimum(1)
        self.distancia_spinBox.setMaximum(10000)
        self.distancia_spinBox.setObjectName(_fromUtf8("distancia_spinBox"))
        self.gridLayout.addWidget(self.distancia_spinBox, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.file_toolButton = QtGui.QToolButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_toolButton.sizePolicy().hasHeightForWidth())
        self.file_toolButton.setSizePolicy(sizePolicy)
        self.file_toolButton.setObjectName(_fromUtf8("file_toolButton"))
        self.gridLayout_2.addWidget(self.file_toolButton, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.file_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.file_lineEdit.setObjectName(_fromUtf8("file_lineEdit"))
        self.gridLayout_2.addWidget(self.file_lineEdit, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.aceptar_pushButton = QtGui.QPushButton(self.frame)
        self.aceptar_pushButton.setObjectName(_fromUtf8("aceptar_pushButton"))
        self.horizontalLayout.addWidget(self.aceptar_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Consulta", None))
        self.label.setText(_translate("Dialog", "Coordenadas:", None))
        self.label_2.setText(_translate("Dialog", "Distancia:", None))
        self.file_toolButton.setText(_translate("Dialog", "...", None))
        self.label_3.setText(_translate("Dialog", "Archivo de Salida:", None))
        self.aceptar_pushButton.setText(_translate("Dialog", "Aceptar", None))

