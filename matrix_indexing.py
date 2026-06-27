board = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

x = int(input("enter row (0-2): "))
y = int(input("enter column (0-2): "))
print(board[x][y])