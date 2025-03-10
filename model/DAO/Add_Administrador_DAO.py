from model.Objects.administrador import Administrador
from dbConnection.FirebaseConnection import FirebaseConnection

class AdministradorDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.administrador_ref = self.firebase_connection.db.collection('administradores')
        else:
            self.administrador_ref = None

    def add_administrador(self, administrador):
        if self.administrador_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(administrador, Administrador):
                raise ValueError(" The object is not an instance of Administrador")
            self.administrador_ref.add(administrador.create_dictionary())
        except Exception as e:
            print(f"Error adding Administrador: {e}")
        
    def get_administradores(self):
        if self.administrador_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.administrador_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Administradores from Firebase: {e}")
            return []