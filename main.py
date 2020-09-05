from flask import Flask, render_template, request, jsonify
import firebase_admin
# from firebase_admin import auth
from firebase_admin import firestore

# Set up Firebase
firebase = firebase_admin.initialize_app()
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup')
def signup():
    # email = request.form.get('email')
    # password = request.form.get('password')
    # # Input validation
    # if email is None or password is None:
    #     return {'message': 'ERROR: Missing email or password'}
    # try:
    #     user = auth.create_user(
    #         email=email,
    #         password=password
    #     )
    #     return {'message': f'Welcome {user.email}'}, 200
    # except:
    #     return {'message': 'ERROR: Cannot create user'}, 400
    return render_template("signup.html")

@app.route('/profiles')
def profiles():
    # profile = []
    # seniors = db.collection(u'seniors').stream()
    # for doc in seniors:
    #     profile.append(doc.to_dict())
    # caregivers = db.collection(u'caregivers').stream()
    # for doc in caregivers:
    #     profile.append(doc.to_dict())
    # return jsonify(profile)
    user = db.collection(u'seniors').document(u'8EOeauhy8ZiDzvd8tTbu').get()
    return render_template("profiles.html", user=user.to_dict())

@app.route('/messages')
def messages():
    return render_template("messages.html")

if __name__ == "__main__":
    app.run(debug=True)
