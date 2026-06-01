# a classroom has:
# 4 rows
# 5 seats in each row
#
# print the classroom layout like this
# Seat 1-1 Seat 1-2 Seat 1-3 Seat 1-4 Seat 1-5
# Seat 2-1 Seat 2-2 Seat 2-3 Seat 2-4 Seat 2-5
# Seat 3-1 Seat 3-2 Seat 3-3 Seat 3-4 Seat 3-5
# Seat 4-1 Seat 4-2 Seat 4-3 Seat 4-4 Seat 4-5

for row in range(1, 5):
    for seat in range(1, 6):
        print(f"Seat {row}-{seat}", end=" ")

    print()