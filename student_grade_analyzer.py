# You are given students and their grades:
# students = {
#     "Anna": [5, 4, 5],
#     "Tom": [3, 4, 2],
#     "Maja": [5, 5, 4]
# }
#
# create a program that:
# prints every student
# prints all grades
# calculates average using FUNCTION
# prints the best student
# prints every grade separately using nested loops

def calculate_average(grades):
    return sum(grades) / len(grades)

students = {
     "Anna": [5, 4, 5],
     "Tom": [3, 4, 2],
     "Maja": [5, 5, 4]
}

best_student = ""
best_average = 0
for student in students:
    grades = students[student]

    average = calculate_average(grades)

    print(student)

    print("Grades:")
    for grade in grades:
        print("-", grade)

    print("Average:", average)

    if average >= best_average:
        best_average = average
        best_student = student


print("Best student:", best_student)
print("Best average:", best_average)