from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.Add_Prestamo_View import Ui_Dialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection

from model.Objects.prestamo import Prestamo
from model.DAO.Add_Prestamo_DAO import PrestamoDAO

class AddPrestamoController(QtWidgets.QDialog):
        
            def __init__(self):
                super().__init__()
                print("I'm adding a new Loan!!!")
                self.ui = Ui_Dialog()
                self.prestamo_dao = PrestamoDAO()
                self.ui.setupUi(self)
                self.initializeGUI()
            
            def initializeGUI(self):
                
                self.ui.btnAddPrestamo.clicked.connect(self.addPrestamo)
                self.ui.le_FechaInicio.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
                self.ui.le_FechaVencimiento.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
                self.ui.le_Estado.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
                self.validateNumber = QRegExpValidator(QRegExp("^[0-9]+$ "), self)
                self.validateStringNoSpaces = QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)
        
            def addPrestamo(self):
                try:
                    fechaInicio = self.ui.le_FechaInicio.text()
                    fechaVencimiento = self.ui.le_FechaVencimiento.text()
                    estado = self.ui.le_Estado.text()
        
                    new_prestamo = Prestamo(fechaInicio,fechaVencimiento,estado)
        
                    if VerifyConnection.verify_connection(self):
                        self.prestamo_dao.add_prestamo(new_prestamo)
        
                        if self.prestamo_dao.prestamo_ref is not None:
                            QMessageBox.information(self, 'Confirmation', "A new Loan has been registered ✔", QMessageBox.Ok)
                        else:
                            QMessageBox.critical(self, "Error",
                                                "Cannot connect to Firebase. Check your Internet connection.",
                                                QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "Error", "No Internet connection. Please check your connection.", QMessageBox.Ok)
        
                    self.clearFields()
                
                except Exception as e:
                    print(f"An error occurred: {e}")
                    QMessageBox.critical(self, "Error", "An unexpected error ocurred while adding the Loan.", QMessageBox.Ok)

            def clearFields(self):
                self.ui.le_FechaInicio.clear()
                self.ui.le_FechaVencimiento.clear()
                self.ui.le_Estado.clear()
                print("Fields cleared")