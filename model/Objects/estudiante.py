from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self,nombre,email,rol):
        super().__init__(nombre, email, rol)

    # Dictionary representation for Firebase
    def create_dictionary(self):
        return {
            "nombre": self.get_nombre(),
            "email": self.get_email(),
            "rol": self.get_rol
        }