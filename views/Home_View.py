from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(728, 585)
        
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 971, 61))
        self.label_title.setStyleSheet("font: 87 18pt 'Arial Black'; background-color: lightblue;")
        self.label_title.setText("Biblioteca Virtual")
        
        self.btnAgregarLibro = QtWidgets.QPushButton(Dialog)
        self.btnAgregarLibro.setGeometry(QtCore.QRect(30, 80, 150, 41))
        self.btnAgregarLibro.setText("Agregar Libro")
        
        self.btnBuscarLibro = QtWidgets.QPushButton(Dialog)
        self.btnBuscarLibro.setGeometry(QtCore.QRect(200, 80, 150, 41))
        self.btnBuscarLibro.setText("Buscar Libro")
        
        self.btnRentarLibro = QtWidgets.QPushButton(Dialog)
        self.btnRentarLibro.setGeometry(QtCore.QRect(370, 80, 150, 41))
        self.btnRentarLibro.setText("Rentar Libro")
        
        self.btnAgregarUsuario = QtWidgets.QPushButton(Dialog)
        self.btnAgregarUsuario.setGeometry(QtCore.QRect(540, 80, 150, 41))
        self.btnAgregarUsuario.setText("Agregar Usuario")
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def abrirAgregarLibro(self):
        print("Abriendo la pantalla para agregar un libro...")
    
    def abrirBuscarLibro(self):
        print("Abriendo la pantalla para buscar un libro...")
    
    def abrirRentarLibro(self):
        print("Abriendo la pantalla para rentar un libro...")
    
    def abrirAgregarUsuario(self):
        print("Abriendo la pantalla para agregar un usuario...")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_HomeView()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
