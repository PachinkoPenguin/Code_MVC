class Prestamo():
    def __init__(self,fechaInicio,fechaVencimiento,estado):
        self.__fechaInicio = fechaInicio
        self.__fechaVencimiento = fechaVencimiento
        self.__estado = estado

    # Getters
    def get_fechaInicio(self):
        return self.__fechaInicio
    
    def get_fechaVencimiento(self):
        return self.__fechaVencimiento
    
    def get_estado(self):
        return self.__estado
    
    # Setters
    def set_fechaInicio(self, fechaInicio):
        self.__fechaInicio = fechaInicio

    def set_fechaVencimiento(self, fechaVencimiento):
        self.__fechaVencimiento = fechaVencimiento

    def set_estado(self, estado):
        self.__estado = estado

    # Dictionary representation for Firebase
    def create_dictionary(self):
        return {
            "fechaInicio": self.__fechaInicio,
            "fechaVencimiento": self.__fechaVencimiento,
            "estado": self.__estado
        }