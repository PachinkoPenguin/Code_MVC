from model.Objects.estudiante import Estudiante
from dbConnection.FirebaseConnection import FirebaseConnection

class EstudianteDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.estudiante_ref = self.firebase_connection.db.collection('estudiantes')
        else:
            self.estudiante_ref = None

    def add_estudiante(self, estudiante):
        if self.estudiante_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(estudiante, Estudiante):
                raise ValueError(" The object is not an instance of Estudiante")
            self.estudiante_ref.add(estudiante.create_dictionary())
        except Exception as e:
            print(f"Error adding Estudiante: {e}")
    
    def get_estudiantes(self):
        if self.estudiante_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.estudiante_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Estudiantes from Firebase: {e}")
            return []