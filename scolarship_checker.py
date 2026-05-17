# You have:
# Student grades
# Attendance percentages
# A student receives a scholarship ONLY IF:
# Grade is grader than 4.5
# AND
# Attendance is greater than 80%
#
# example:
# names = ["Anna", "Tom", "Maja"]
# grades = [4.8, 4.2, 5.0]
# attendance = [90, 95, 70]
# Program should print students who qualify

names = ["Anna", "Tom", "Maja"]
grades = [4.8, 4.2, 5.0]
attendance = [90, 95, 70]

for i in range(len(names)):
    if grades[i] > 4.5 and attendance[i] > 80:
        print(f" {names[i]} qualifies for the scholarship")