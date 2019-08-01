from google.cloud import firestore
from google.auth import credentials

cred = credentials.ApplicationDefault()
firestore.initialize_app(cred, {
	'apiKey': "AIzaSyA7MjB3---S-sF4w9APspbbgnVhEATsnqE",
    'authDomain': "checkpoint-scanner.firebaseapp.com",
    'databaseURL': "https://checkpoint-scanner.firebaseio.com",
    'projectId': "checkpoint-scanner",
    'storageBucket': "",
    'messagingSenderId': "911155687813",
    'appId': "1:911155687813:web:328b6839734e72d8"
})

db = firestore.Client()

print (db)