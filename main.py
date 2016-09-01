import sys
import os
from designer.gui import *
import PyQt4



class Antecedentes(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.fileDialog = QtGui.QFileDialog(self)
        self.fileDialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        self.ui.aceptar_pushButton.setFocus()
        self.ui.coordenadas_lineEdit.setPlaceholderText('-34.642526, -58.376055')



        QtCore.QObject.connect(self.ui.file_toolButton,
                               QtCore.SIGNAL('clicked()'),
                               self.x)
        QtCore.QObject.connect(self.ui.aceptar_pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.x)


    def x(self):
        fn = QtGui.QFileDialog.getSaveFileName(self, 'a')
        print(fn)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    antecedentes = Antecedentes()
    antecedentes.show()
    sys.exit(app.exec_())