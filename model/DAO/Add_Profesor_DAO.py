from model.Objects.profesor import Profesor
from dbConnection.FirebaseConnection import FirebaseConnection

class ProfesorDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.profesor_ref = self.firebase_connection.db.collection('profesores')
        else:
            self.profesor_ref = None

    def add_profesor(self, profesor):
        if self.profesor_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(profesor, Profesor):
                raise ValueError(" The object is not an instance of Profesor")
            self.profesor_ref.add(profesor.create_dictionary())
        except Exception as e:
            print(f"Error adding Profesor: {e}")
        
    def get_profesores(self):
        if self.profesor_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.profesor_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Profesores from Firebase: {e}")