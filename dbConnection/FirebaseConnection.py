import os
import firebase_admin
from firebase_admin import credentials, firestore


class FirebaseConnection:
    def __init__(self):
        try:
            # Get the path of the folder where the script is located
            base_dir = os.path.dirname(os.path.abspath(__file__))

            # Create the path to the JSON file, assuming it is in the same folder as the script
            json_filename = "credentials/firebase_credentials.json"
            json_path = os.path.join(base_dir,json_filename)

            # Verify that the JSON file exists
            if not os.path.exists(json_path):
                print(f" Credential file not found in {json_path}")
                raise FileNotFoundError(f"Credential file not found in {json_path}")

            # Initialize Firebase only if it has not been initialized before
            if not firebase_admin._apps:
                cred = credentials.Certificate(json_path)
                firebase_admin.initialize_app(cred)
                print("Successful connection to Firebase.")
            else:
                print("Firebase connection is already initialized.")

            # Connect to Firestore
            self.db = firestore.client()

        except Exception as e:
            print(f" Error connecting to Firebase: {e}")
            self.db = None


# Using the class
firebase_connection = FirebaseConnection()

