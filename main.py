import sys
from designer.gui import *
from consultas import make_query


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
                               self.pick_file_name)
        QtCore.QObject.connect(self.ui.aceptar_pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.save_file)

    def clear_form(self):
        self.ui.coordenadas_lineEdit.clear()
        self.ui.distancia_spinBox.setValue(1)
        self.ui.file_lineEdit.clear()

    def pick_file_name(self):
        fn = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Archivo')
        self.ui.file_lineEdit.setText(fn + '.csv')

    def save_file(self):
        coords = self.ui.coordenadas_lineEdit.text()
        distancia = self.ui.distancia_spinBox.value()
        path = self.ui.file_lineEdit.text()
        make_query(coords, distancia, path)
        self.clear_form()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    antecedentes = Antecedentes()
    antecedentes.show()
    sys.exit(app.exec_())
