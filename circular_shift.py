names = ["Anna", "Tom", "Maja"]

for i in range(0, len(names)):
    if i != len(names)-1:
        print(f"{names[i]} -> {names[i+1]}")
    else:
        print(print(f"{names[i]} -> {names[0]}"))