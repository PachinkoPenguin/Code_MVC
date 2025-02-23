from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controllers.calculadora.calculador import Calculadora

class CalculatorController(QtWidgets.QMainWindow, Calculadora):

    def __init__(self):
        super().__init__()
        self.ui.setupUi(self)
        self.initializeGUI()

    # Conectar botones a funciones
    def initializeGUI(self):
        self.ui.btnSum.clicked.connect(lambda: self.calculate("sumar"))
        self.ui.btnSub.clicked.connect(lambda: self.calculate("restar"))
        

    # Método para obtener los valores de los QLineEdit
    def getValues(self):
        try:
            a = float(self.ui.txtNum1.text())
            b = float(self.ui.txtNum2.text())
            return a, b
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")
            return None, None

    # Implementación del método abstracto operacion()
    def operacion(self, tipo, a, b):
        if tipo == "sumar":
            return a + b
        elif tipo == "restar":
            return a - b
        else:
            return "Operación no válida"

    # Llama a la operación y muestra el resultado
    def calculate(self, tipo):
        a, b = self.getValues()
        if a is not None and b is not None:
            resultado = self.operacion(tipo, a, b)
            self.ui.txtResult.setText(str(resultado))
