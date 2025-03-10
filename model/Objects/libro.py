class Libro:
    def __init__(self,titulo,autor,genero,estado):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__estado = estado
    
    # Getters
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_genero(self):
        return self.__genero
    
    def get_estado(self):
        return self.__estado
    
    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_genero(self, genero):
        self.__genero = genero
    
    def set_estado(self, estado):
        self.__estado = estado

    # Dictionary representation for Firebase
    def create_dictionary(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "estado": self.__estado
        }