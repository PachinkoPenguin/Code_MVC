from model.Objects.libro import Libro
from dbConnection.FirebaseConnection import FirebaseConnection

class LibroDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.libro_ref = self.firebase_connection.db.collection('libros')
        else:
            self.libro_ref = None

    def add_libro(self, libro):
        if self.libro_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(libro, Libro):
                raise ValueError(" The object is not an instance of Libro")
            self.libro_ref.add(libro.create_dictionary())
        except Exception as e:
            print(f"Error adding Libro: {e}")

    def get_libros(self):
        if self.libro_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.libro_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Libros from Firebase: {e}")
            return []