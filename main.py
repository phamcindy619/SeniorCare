from flask import Flask, render_template, request, jsonify
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
    profile = []
    seniors = db.collection(u'seniors').stream()
    for doc in seniors:
        profile.append(doc.to_dict())
    caregivers = db.collection(u'caregivers').stream()
    for doc in caregivers:
        profile.append(doc.to_dict())
    return jsonify(profile)

if __name__ == "__main__":
    app.run(debug=True)
