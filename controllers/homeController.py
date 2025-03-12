from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from views.Home_View import Ui_HomeView
from views.agregarLibro import Ui_AgregarLibro
from views.vistaSolicitarPrestamo import Ui_BuscarLibro
from views.agregarUsuario import Ui_AgregarUsuario  # Import new view
from controllers.AddUsuarioController import AddUsuarioController  # Import new controller

from controllers.AddLibroController import AddLibroController

class HomeController(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("Iniciando la Biblioteca Virtual")
        self.ui = Ui_HomeView()
        self.ui.setupUi(self)
        self.initializeGUI()

    def initializeGUI(self):
        """ Conectar botones a sus funciones """
        self.ui.btnAgregarLibro.clicked.connect(self.abrirAgregarLibro)
        self.ui.btnBuscarLibro.clicked.connect(self.abrirBuscarLibro)
        self.ui.btnRentarLibro.clicked.connect(self.abrirRentarLibro)
        self.ui.btnAgregarUsuario.clicked.connect(self.abrirAgregarUsuario)  # New Button Connection

    def abrirAgregarLibro(self):
        addlibroController = AddLibroController()
        addlibroController.exec_()

    def abrirBuscarLibro(self):
        """ Abre la ventana para buscar un libro """
        ventanaBuscar = QDialog()
        uiBuscar = Ui_BuscarLibro()
        uiBuscar.setupUi(ventanaBuscar)
        ventanaBuscar.exec_()

    def abrirRentarLibro(self):
        """ Esta función puede ser implementada más adelante """
        print("Función de renta de libros aún no implementada.")

    def abrirAgregarUsuario(self):
        """ Abre la ventana para agregar un usuario """
        addUsuarioController = AddUsuarioController()
        addUsuarioController.exec_()
