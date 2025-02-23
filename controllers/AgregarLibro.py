from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from views.agregarLibro import Ui_Dialog


class AgregarLibroCotroller(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        print("I'm adding a new Nakama :D")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initializeGUI()

    # Initialize elements, for example, setting up button functionality
    def initializeGUI(self):

        self.ui.btnAgregar.clicked.connect(self.agregarLibro)

    def agregarLibro(self):

        
