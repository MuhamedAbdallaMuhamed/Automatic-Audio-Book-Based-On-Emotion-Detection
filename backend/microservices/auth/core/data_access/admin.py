import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from config import config

import os


cred = credentials.Certificate(os.path.realpath("config/serviceAccountKey.json"))

firebase = pyrebase.initialize_app(config)
firebase_admin.initialize_app(cred)

db = firestore.client()
db_storage = firebase.storage()
image_ref = db_storage.child('images')
