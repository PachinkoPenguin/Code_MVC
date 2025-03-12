from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.agregarUsuario import Ui_AgregarUsuario as Ui_Dialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection

from model.Objects.usuario import Usuario
from model.DAO.Add_Usuario_DAO import UsuarioDAO

class AddUsuarioController(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        print("I'm adding a new User!!!")
        self.ui = Ui_Dialog()
        self.usuario_dao = UsuarioDAO()
        self.ui.setupUi(self)
        self.initializeGUI()
    
    def initializeGUI(self):
        print("Connecting buttons to functions...")
        self.ui.btnAddUsuario.clicked.connect(self.addUsuario)
        self.ui.le_Nombre.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
        self.ui.le_Email.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
        self.ui.le_Rol.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
        self.validateNumber = QRegExpValidator(QRegExp("^[0-9]+$ "), self)
        self.validateStringNoSpaces = QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)

    def addUsuario(self):
        try:
            name = self.ui.le_Nombre.text()
            email = self.ui.le_Email.text()
            rol = self.ui.le_Rol.text()

            new_usuario = Usuario(name,email,rol)

            if VerifyConnection.verify_connection(self):
                self.usuario_dao.add_usuario(new_usuario)

                if self.usuario_dao.usuario_ref is not None:
                    QMessageBox.information(self, 'Confirmation', "A new User has been registered ", QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error",
                                         "Cannot connect to Firebase. Check your Internet connection.",
                                         QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Error", "No Internet connection. Please check your connection.", QMessageBox.Ok)

            self.clearFields()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            QMessageBox.critical(self, "Error", "An unexpected error ocurred while adding the User.", QMessageBox.Ok)

    def clearFields(self):
        self.ui.le_Nombre.clear()
        self.ui.le_Email.clear()
        self.ui.le_Rol.clear()
        print("Fields cleared")