class Usuario:
    def __init__(self, nombre,email,rol):
        self.__nombre = nombre
        self.__email = email
        self.__rol = rol

    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def get_rol(self):
        return self.__rol

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def set_rol(self, rol):
        self.__rol = rol

    # Dictionary representation for Firebase
    def create_dictionary(self):
        return {
            "nombre": self.__nombre,
            "email": self.__email,
            "rol": self.__rol
        }


