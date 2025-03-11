from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controllers.AddNakamaController import AddNakamaController
from controllers.AddLibroController import AddLibroController
from controllers.AddAdministradorController import AddAdministradorController
from controllers.AddEstudianteController import AddEstudianteController
from controllers.AddLaptopController import AddLaptopController
from controllers.AddPrestamoController import AddPrestamoController
from controllers.AddProfesorController import AddProfesorController
from controllers.AddUsuarioController import AddUsuarioController

from views.Home_View import Ui_Dialog

class HomeController(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("I'm adding a new Nakama :D")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initializeGUI()

    # Initialize elements, for example, setting up button functionality
    def initializeGUI(self):

        self.ui.btnOpenAddNakama.clicked.connect(self.abrirAddNakama)
        self.ui.btnOpenAgregarLibro.clicked.connect(self.abrirAddLibro)
        self.ui.btnOpenBuscarLibro.clicked.connect(self.)
        self.ui.btnOpenRentarLibro.clicked.connect(self.)
        self.ui.btnOpenAddAdministrador.clicked.connect(self.abrirAddAdministrador)
        self.ui.btnOpenAddEstudiante.clicked.connect(self.abrirAddEstudiante)
        self.ui.btnOpenAddLaptop.clicked.connect(self.abrirAddLaptop)
        self.ui.btnOpenAddPrestamo.clicked.connect(self.abrirAddPrestamo)
        self.ui.btnOpenAddProfesor.clicked.connect(self.abrirAddProfesor)
        self.ui.btnOpenAddUsuario.clicked.connect(self.abrirAddUsuario)

    def abrirAddNakama(self):

        firstController = AddNakamaController()
        firstController.exec_()

    def abrirAddLibro(self):
        
        firstController = AddLibroController()
        firstController.exec_()

    def abrirBuscarLibro(self):

        firstController = AddLibroController()
        firstController.exec_()

    def abrirRentarLibro(self):
        
        firstController = AddLibroController()
        firstController.exec_()

    def abrirAddAdministrador(self):
            
        firstController = AddAdministradorController()
        firstController.exec_()

    def abrirAddEstudiante(self):

        firstController = AddEstudianteController()
        firstController.exec_()

    def abrirAddLaptop(self):
    
        firstController = AddLaptopController()
        firstController.exec_()

    def abrirAddPrestamo(self):

        firstController = AddPrestamoController()
        firstController.exec_()

    def abrirAddProfesor(self):
        
        firstController = AddProfesorController()
        firstController.exec_()

    def abrirAddUsuario(self):
    
        firstController = AddUsuarioController()
        firstController.exec_()