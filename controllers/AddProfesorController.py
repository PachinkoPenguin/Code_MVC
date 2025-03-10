from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.Add_Profesor_View import Ui_Dialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection

from model.Objects.profesor import Profesor
from model.DAO.Add_Profesor_DAO import ProfesorDAO

class AddProfesorController(QtWidgets.QDialog):
        
            def __init__(self):
                super().__init__()
                print("I'm adding a new Teacher!!!")
                self.ui = Ui_Dialog()
                self.profesor_dao = ProfesorDAO()
                self.ui.setupUi(self)
                self.initializeGUI()
            
            def initializeGUI(self):
                
                self.ui.btnAddProfesor.clicked.connect(self.addProfesor)
                self.ui.le_Nombre.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
                self.ui.le_Email.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
                self.ui.le_Rol.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
                self.validateNumber = QRegExpValidator(QRegExp("^[0-9]+$ "), self)
                self.validateStringNoSpaces = QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)
        
            def addProfesor(self):
                try:
                    name = self.ui.le_Nombre.text()
                    email = self.ui.le_Email.text()
                    rol = self.ui.le_Rol.text()
        
                    new_profesor = Profesor(name,email,rol)
        
                    if VerifyConnection.verify_connection(self):
                        self.profesor_dao.add_profesor(new_profesor)
        
                        if self.profesor_dao.profesor_ref is not None:
                            QMessageBox.information(self, 'Confirmation', "A new Teacher has been registered ✔", QMessageBox.Ok)
                        else:
                            QMessageBox.critical(self, "Error",
                                                "Cannot connect to Firebase. Check your Internet connection.",
                                                QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "Error", "No Internet connection. Please check your connection.", QMessageBox.Ok)
        
                    self.clearFields()
                
                except Exception as e:
                    print(f"An error occurred: {e}")
                    QMessageBox.critical(self, "Error", "An unexpected error ocurred while adding the Teacher.", QMessageBox.Ok)
        
            def clearFields(self):
                self.ui.le_Nombre.clear()
                self.ui.le_Email.clear()
                self.ui.le_Rol.clear()
                print("Fields cleared")