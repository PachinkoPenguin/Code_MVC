class Laptop():
    def __init__(self,marca,modelo,estado):
        self.__marca = marca
        self.__modelo = modelo
        self.__estado = estado

    # Getters
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_estado(self):
        return self.__estado
    
    # Setters

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_estado(self, estado):
        self.__estado = estado

    # Dictionary representation for Firebase
    def create_dictionary(self):
        return {
            "marca": self.__marca,
            "modelo": self.__modelo,
            "estado": self.__estado
        }