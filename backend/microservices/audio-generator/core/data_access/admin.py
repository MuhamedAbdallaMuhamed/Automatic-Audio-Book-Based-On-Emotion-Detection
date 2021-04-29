import firebase_admin
from firebase_admin import firestore, storage
import pyrebase

from config import config

firebase = pyrebase.initialize_app(config)
firebase_admin.initialize_app()

db = firestore.client()
db_storage = firebase.storage()
image_ref = db_storage

app = firebase_admin.initialize_app(options={"storageBucket": "auto-audio-book-with-emotion.appspot.com"}, name="storage")
bucket = storage.bucket(app=app)