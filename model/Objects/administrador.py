from usuario import Usuario

class Administrador(Usuario):
    def __init__(self,nombre,email,rol, nivelAcceso):
        super().__init__(nombre, email, rol)
        self.__nivelAcceso = nivelAcceso

    # Getters
    def get_nivelAcceso(self):
        return self.__nivelAcceso
    
    # Setters
    def set_nivelAcceso(self, nivelAcceso):
        self.__nivelAcceso = nivelAcceso

    # Dictionary representation for Firebase
    def create_dictionary(self):
        return {
            "nombre": self.get_nombre(),
            "email": self.get_email(),
            "rol": self.get_rol(),
            "nivelAcceso": self.__nivelAcceso
        }