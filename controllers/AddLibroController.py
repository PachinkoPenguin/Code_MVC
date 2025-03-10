from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.Add_Libro_View import Ui_Dialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from dbConnection.VerifyConnection import VerifyConnection

from model.Objects.libro import Libro
from model.DAO.Add_Libro_DAO import LibroDAO

class AddLibroController(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        print("I'm adding a new Book!!!")
        self.ui = Ui_Dialog()
        self.libro_dao = LibroDAO()
        self.ui.setupUi(self)
        self.initializeGUI()
    
    def initializeGUI(self):
        
        self.ui.btnAddLibro.clicked.connect(self.addLibro)
        self.ui.le_Title.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
        self.ui.le_Author.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
        self.ui.le_Genre.setStyleSheet("QLineEdit { font-family: Arial; font-size: 16px; font-style: italic; }")
        self.validateNumber = QRegExpValidator(QRegExp("^[0-9]+$ "), self)
        self.validateStringNoSpaces = QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)

    def addLibro(self):
        try:
            title = self.ui.le_Title.text()
            author = self.ui.le_Author.text()
            genre = self.ui.le_Genre.text()

            new_libro = Libro(title,author,genre)

            if VerifyConnection.verify_connection(self):
                self.libro_dao.add_libro(new_libro)

                if self.libro_dao.libro_ref is not None:
                    QMessageBox.information(self, 'Confirmation', "A new Book has been registered ✔", QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error",
                                         "Cannot connect to Firebase. Check your Internet connection.",
                                         QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Error", "No Internet connection. Please check your connection.", QMessageBox.Ok)

            self.clearFields()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            QMessageBox.critical(self, "Error", "An unexpected error ocurred while adding the Book.", QMessageBox.Ok)

    def clearFields(self):
        self.ui.le_Title.clear()
        self.ui.le_Author.clear()
        self.ui.le_Genre.clear()
        print("Fields cleared")