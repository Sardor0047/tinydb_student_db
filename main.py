from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json')
student1 = {
    "id": 4711,
    "name": "Sardor",
    "age": 18,
    "gender": "Male",
    "contact": "+998904624711",
    "grade_level": "Grade 12",
    "subjects": {
        "math": 89,
        "science": 90,
        "english": 88
    },
    "attendance": 98.9,
    "activities": ["Valeball", "Debate Club","Football"],
    "address": {
        "street": "Satepo",
        "city": "Samarqand",
        "state": "UZ",
        "zip_code": "074733"
    }
}

students_table = db.table('students')


db.insert(student1)
