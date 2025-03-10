from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.Add_Laptop_View import Ui_Dialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection

from model.Objects.laptop import Laptop
from model.DAO.Add_Laptop_DAO import LaptopDAO

class AddLaptopController(QtWidgets.QDialog):
    
        def __init__(self):
            super().__init__()
            print("I'm adding a new Laptop!!!")
            self.ui = Ui_Dialog()
            self.laptop_dao = LaptopDAO()
            self.ui.setupUi(self)
            self.initializeGUI()
        
        def initializeGUI(self):
            
            self.ui.btnAddLaptop.clicked.connect(self.addLaptop)
            self.ui.le_Marca.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
            self.ui.le_Modelo.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
            self.ui.le_Estado.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
            self.validateNumber = QRegExpValidator(QRegExp("^[0-9]+$ "), self)
            self.validateStringNoSpaces = QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)
    
        def addLaptop(self):
            try:
                marca = self.ui.le_Marca.text()
                modelo = self.ui.le_Modelo.text()
                estado = self.ui.le_Estado.text()
    
                new_laptop = Laptop(marca,modelo,estado)
    
                if VerifyConnection.verify_connection(self):
                    self.laptop_dao.add_laptop(new_laptop)
    
                    if self.laptop_dao.laptop_ref is not None:
                        QMessageBox.information(self, 'Confirmation', "A new Laptop has been registered ✔", QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "Error",
                                            "Cannot connect to Firebase. Check your Internet connection.",
                                            QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "No Internet connection. Please check your connection.", QMessageBox.Ok)
    
                self.clearFields()
            
            except Exception as e:
                print(f"An error occurred: {e}")
                QMessageBox.critical(self, "Error", "An unexpected error ocurred while adding the Laptop.", QMessageBox.Ok)
    
        def clearFields(self):
            self.ui.le_Marca.clear()
            self.ui.le_Modelo.clear()
            self.ui.le_Estado.clear()
            print("Fields cleared")