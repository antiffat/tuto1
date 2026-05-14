total_price = 0.0
while True:
    input_field = input("please enter the item's price: ")
    if (input_field.lower() == "done"):
        print(f"Your total price: {total_price}")
        break

    price = float(input_field)
    total_price += price

