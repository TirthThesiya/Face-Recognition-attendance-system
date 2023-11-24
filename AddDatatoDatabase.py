import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance-7aeb4-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Meet Gorasiya",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-21 00:54:34"
        },
    "2":
        {
            "name": "Parth Sadigale",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-11-21 00:54:34"
        },
    "3":
        {
            "name": "Prapti Deshmukh",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 17,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-21 00:54:34"
        },
    "4":
        {
            "name": "Shivraj Ghorpode",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-21 00:54:34"
        },
    "5":
        {
            "name": "Tirth Thesiya",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 25,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-21 00:54:34"
        },
    "6":
        {
            "name": "Dhruv Sakariya",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 20,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-21 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)