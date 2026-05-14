# Create a program that:
# asks for student grades until user types "done"
# stores grades in a list
# prints:
# - average
# - highest grade
# - lowest grade
# - all grades above average

grades = []

while True:
    grade = input("Enter a grade (or type done): ")

    if grade.lower() == "done":
        break

    grade = float(grade)
    grades.append(grade)

    total = sum(grades)
    length = len(grades)
    avg = total/length

    highest = max(grades)
    lowest = min(grades)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

    for grade in grades:
        if grade > avg:
            print(grade)