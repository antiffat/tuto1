# A tic-tac-toe board is stored as a list of lists.
# board = [
#     ["X", "O", "X"],
#     [" ", "X", "O"],
#     ["O", " ", "X"]
# ]
# Create a program that prints the board nicely:
# X O X
#  X O
# O   X

board = [
     ["X", "O", "X"],
     [" ", "X", "O"],
     ["O", " ", "X"]
]

for row in board:
    for cell in row:
        print(cell, end=" ")
    print()