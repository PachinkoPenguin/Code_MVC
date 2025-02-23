from abc import ABC, abstractmethod

class Calculadora(ABC):
    """Clase abstracta que define un método genérico para operar"""

    @abstractmethod
    def operacion(self, tipo, a, b):
        pass
