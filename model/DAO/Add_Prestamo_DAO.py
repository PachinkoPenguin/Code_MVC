from model.Objects.prestamo import Prestamo
from dbConnection.FirebaseConnection import FirebaseConnection

class PrestamoDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.prestamo_ref = self.firebase_connection.db.collection('prestamos')
        else:
            self.prestamo_ref = None

    def add_prestamo(self, prestamo):
        if self.prestamo_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(prestamo, Prestamo):
                raise ValueError(" The object is not an instance of Prestamo")
            self.prestamo_ref.add(prestamo.create_dictionary())
        except Exception as e:
            print(f"Error adding Prestamo: {e}")
    
    def get_prestamos(self):
        if self.prestamo_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.prestamo_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Prestamos from Firebase: {e}")
            return []