from model.Objects.usuario import Usuario
from dbConnection.FirebaseConnection import FirebaseConnection

class UsuarioDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.usuario_ref = self.firebase_connection.db.collection('usuarios')
        else:
            self.usuario_ref = None

    def add_usuario(self, usuario):
        if self.usuario_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(usuario, Usuario):
                raise ValueError(" The object is not an instance of Usuario")
            self.usuario_ref.add(usuario.create_dictionary())
        except Exception as e:
            print(f"Error adding Usuario: {e}")
        
    def get_usuarios(self):
        if self.usuario_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.usuario_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Usuarios from Firebase: {e}")
            return []