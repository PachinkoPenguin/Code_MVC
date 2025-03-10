from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.Add_Estudiante_View import Ui_Dialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection

from model.Objects.estudiante import Estudiante
from model.DAO.Add_Estudiante_DAO import EstudianteDAO

class AddEstudianteController(QtWidgets.QDialog):
    
        def __init__(self):
            super().__init__()
            print("I'm adding a new Student!!!")
            self.ui = Ui_Dialog()
            self.estudiante_dao = EstudianteDAO()
            self.ui.setupUi(self)
            self.initializeGUI()
        
        def initializeGUI(self):
            
            self.ui.btnAddEstudiante.clicked.connect(self.addEstudiante)
            self.ui.le_Nombre.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
            self.ui.le_Email.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
            self.ui.le_Rol.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
            self.validateNumber = QRegExpValidator(QRegExp("^[0-9]+$ "), self)
            self.validateStringNoSpaces = QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)
    
        def addEstudiante(self):
            try:
                name = self.ui.le_Nombre.text()
                email = self.ui.le_Email.text()
                rol = self.ui.le_Rol.text()
    
                new_estudiante = Estudiante(name,email,rol)
    
                if VerifyConnection.verify_connection(self):
                    self.estudiante_dao.add_estudiante(new_estudiante)
    
                    if self.estudiante_dao.estudiante_ref is not None:
                        QMessageBox.information(self, 'Confirmation', "A new Student has been registered ✔", QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "Error",
                                            "Cannot connect to Firebase. Check your Internet connection.",
                                            QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "No Internet connection. Please check your connection.", QMessageBox.Ok)
    
                self.clearFields()
            
            except Exception as e:
                print(f"An error occurred: {e}")
                QMessageBox.critical(self, "Error", "An unexpected error ocurred while adding the Student.", QMessageBox.Ok)
    
        def clearFields(self):
            self.ui.le_Nombre.clear()
            self.ui.le_Email.clear()
            self.ui.le_Rol.clear()
            print("Fields cleared")