ratings = []

while True:
    rating = input("Enter rating (or done): ")

    if rating == "done":
        break

    rating = float(rating)
    ratings.append(rating)

print("\nRatings:", ratings)

average = sum(ratings) / len(ratings)
highest = max(ratings)
lowest = min(ratings)

above_average = 0
below_average = 0

for rating in ratings:
    if rating > average:
        above_average += 1
    elif rating < average:
        below_average += 1

print("\nAverage:", average)
print("Highest:", highest)
print("Lowest:", lowest)

print("\nAbove average:", above_average)
print("Below average:", below_average)