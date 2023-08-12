import os

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

__current_path = os.path.dirname(os.path.abspath(__file__))
firebase_key_path = os.path.join(__current_path, "firebase-service-key.json")

cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred)

__db = firestore.client()


def use_database():
    return __db
