from model.Objects.laptop import Laptop
from dbConnection.FirebaseConnection import FirebaseConnection

class LaptopDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.laptop_ref = self.firebase_connection.db.collection('laptops')
        else:
            self.laptop_ref = None

    def add_laptop(self, laptop):
        if self.laptop_ref is None:
            print(" Cannot connect to Firebase....")
            return
        
        try:
            if not isinstance(laptop, Laptop):
                raise ValueError(" The object is not an instance of Laptop")
            self.laptop_ref.add(laptop.create_dictionary())
        except Exception as e:
            print(f"Error adding Laptop: {e}")

    def get_laptops(self):
        if self.laptop_ref is None:
            print("Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.laptop_ref.stream()]
        except Exception as e:
            print(f"Error retrieving Laptops from Firebase: {e}")
            return []