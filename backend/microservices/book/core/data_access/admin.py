import firebase_admin
from firebase_admin import firestore, storage
import pyrebase
import os
from firebase_admin import credentials, firestore, storage

from config import config

cred = credentials.Certificate(os.path.realpath("E:/Graduation Project/Automatic-Audio-Book-Based-On-Emotion-Detection/backend/microservices/book/config/serviceAccountKey.json"))

firebase = pyrebase.initialize_app(config)
firebase_admin.initialize_app(cred)

db = firestore.client()
db_storage = firebase.storage()
image_ref = db_storage

app = firebase_admin.initialize_app(cred, options={"storageBucket": "auto-audio-book-with-emotion.appspot.com"}, name="storage")
bucket = storage.bucket(app=app)