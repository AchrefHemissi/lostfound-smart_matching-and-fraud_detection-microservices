from app.services.clip_service import create_clip_embedding
from app.services.vector_service import qdrant_store, qdrant_search
import firebase_admin
from firebase_admin import credentials, firestore
import requests

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_firebase_post(post_id: str):
    doc = db.collection("posts").document(post_id).get()
    if doc.exists:
        return doc.to_dict()
    return None

def generate_embedding(image_url: str, text: str):
    response = requests.get(image_url)
    image_bytes = response.content #Extracts the raw image content (in bytes) from the HTTP response.
    return create_clip_embedding(image_bytes, text)

def store_embedding(post_id: str, embedding, metadata):
    qdrant_store(post_id, embedding, metadata)

def find_similar_embeddings(post_id: str):
    return qdrant_search(post_id)
