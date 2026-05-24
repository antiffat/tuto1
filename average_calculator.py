# create a function called calculate_average that:
# receives  a list
# returns average
#
# then use it with:
# grades
# ratings

def calculate_average(nums):
    average = sum(nums) / len(nums)
    return average

grades = [3.5, 3.3, 2.0, 5.0]
print(calculate_average(grades))

