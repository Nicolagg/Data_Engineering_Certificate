# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('Part 4/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://assignment-module12-1b771-default-rtdb.firebaseio.com/'
})
# save data
ref = db.reference('business/')
users_ref = ref.child('CEO')
users_ref.set({
    'elonmusk': {
        'date_of_birth': 'June 28, 1971',
        'full_name': 'Elon Musk',
        'nationality': 'South African'
    },
    'jeffbezos': {
        'date_of_birth': 'January 12, 1964',
        'full_name': 'Jeff Bezos',
        'nationality': 'American'
    }
})

# update data
hopper_ref = users_ref.child('jeffbezos')
hopper_ref.update({
    'occupation': 'Entrepreneur'})
# read data
handle = db.reference('business/CEO/elonmusk')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())