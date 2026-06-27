flat_coords = [0, 0, 0, 2, 2, 2, 2, 0]

for i in range(0, len(flat_coords), 2):
    x = flat_coords[i]
    y = flat_coords[i+1]
    print("Point:", x, y)

