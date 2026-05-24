# print multiplication table from 1 to 5.

# ixj
# 1x1 1x2 1x3 1x4 1x5
# 2x1 2x2 2x3 2x4 2x5
# 3x1 3x2 3x3 3x4 3x5

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")

    print()
