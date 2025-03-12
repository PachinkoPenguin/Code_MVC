from PyQt5 import QtCore, QtWidgets

class Ui_AgregarUsuario(object):
    def setupUi(self, AgregarUsuarioDialog):
        AgregarUsuarioDialog.setObjectName("AgregarUsuarioDialog")
        AgregarUsuarioDialog.resize(400, 400)

        self.label = QtWidgets.QLabel(AgregarUsuarioDialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 221, 71))
        self.label.setStyleSheet("font: 75 16pt 'MS Shell Dlg 2';")
        self.label.setText("Agregar Usuario")
        
        self.le_Nombre = QtWidgets.QLineEdit(AgregarUsuarioDialog)
        self.le_Nombre.setGeometry(QtCore.QRect(50, 50, 100, 30))
        self.le_Nombre.setPlaceholderText("Nombre:")
        
        self.le_Email = QtWidgets.QLineEdit(AgregarUsuarioDialog)
        self.le_Email.setGeometry(QtCore.QRect(50, 100, 100, 30))
        self.le_Email.setPlaceholderText("Email:")
        
        self.le_Rol = QtWidgets.QLineEdit(AgregarUsuarioDialog)
        self.le_Rol.setGeometry(QtCore.QRect(50, 150, 100, 30))
        self.le_Rol.setPlaceholderText("Rol:")
        
        self.btnAddUsuario = QtWidgets.QPushButton(AgregarUsuarioDialog)
        self.btnAddUsuario.setGeometry(QtCore.QRect(150, 250, 100, 40))
        self.btnAddUsuario.setText("Guardar")

        QtCore.QMetaObject.connectSlotsByName(AgregarUsuarioDialog)
