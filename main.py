from flask import Flask, render_template, request, json
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore

# Set up Firebase
default_app = firebase_admin.initialize_app()
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/signup')
def signup():
    return 'Please sign up.'

@app.route('/login')
def login():
    return 'Please login.'

@app.route('/profiles')
def profiles():
    profiles = []
    docs = db.collection(u'seniors').stream()
    for doc in docs:
        profiles.append(json.loads(doc))
    return json.dumps(profiles)

if __name__ == "__main__":
    app.run(debug=True)
