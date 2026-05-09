vip_names= ["Alice", "Bob", "Fatima"]

while True:
    name = input("What is your name? ")

    if name.lower() == "exit":
        print("good bye!")
        break

    if name in vip_names:
        print(f"Access granted, you are in, {name}")
    else:
        print("Access denied, you are not in")