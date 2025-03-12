from model.Objects.usuario import Usuario
from dbConnection.FirebaseConnection import FirebaseConnection

class UsuarioDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.usuario_ref = self.firebase_connection.db.collection("usuarios")  # ✅ Ensure collection name is correct
        else:
            self.usuario_ref = None

    def add_usuario(self, usuario):
        if self.usuario_ref is None:
            print(" Cannot connect to Firebase....")
            return

        try:
            if not isinstance(usuario, Usuario):
                raise ValueError(" The object is not an instance of Usuario")

            print(f" Saving Usuario to Firestore: {usuario.create_dictionary()}")  # ✅ Debug Print

            # ✅ Save to Firestore, using email as document ID
            doc_ref = self.usuario_ref.document(usuario.get_email())  # ✅ Email is unique ID
            doc_ref.set(usuario.create_dictionary())  # ✅ .set() updates or creates the document

            print(f"✅ User successfully saved: {usuario.get_email()}")

        except Exception as e:
            print(f" Error adding Usuario: {e}")
