
names = ["Anna", "Tom", "Maja"]
grades = [4.8, 4.2, 5.0]
attendance = [90, 95, 70]

# key -> value
student = {
    "name": "Anna",
    "grade": 4.8,
    "attendance": 90
}

print(student["name"])
student["grade"] = 4.5
student["university"] = "PJATK"
print(student)
for key in student:
    print(key, student[key])


students = [
    {"name": "Anna",
     "grade": 4.8,
     "attendance": 90},

    {"name": "Tom",
     "grade": 4.8,
     "attendance": 90},

    {"name": "Maja",
     "grade": 4.8,
     "attendance": 90}
]