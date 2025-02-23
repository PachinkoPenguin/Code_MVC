from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection
from controllers.AddNakamaController import AddNakamaController
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

    def abrirAddNakama(self):

        firstController = AddNakamaController()
        firstController.exec_()

    

