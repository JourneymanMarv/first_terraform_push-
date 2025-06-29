students = [ 
    {"name":"Mark", "grade": 90},
    {"name": "James", "grade": 70}, 
    {"name": "James", "grade": 80}
]

for student in students: 
    name = student["name"]
    student_grade = student["grade"]
    if student_grade > 70:
        print("good grade")
    else: 
        print("do better")