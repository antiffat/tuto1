# An online shop stores purchases like this:
# orders = {
#     "Alice": ["Laptop", "Mouse"],
#     "Bob": ["Keyboard"],
#     "Charlie": ["Monitor", "Mouse", "Laptop"]
# }
#
# Create a program that:
# prints every customer
# prints all products bought by that customer
# calculates how many products each customer bought
# prints the customer who bought the most products
# Requirements:
# use a function
# use a dictionary
# use nested loops

def count_products(products):
    return len(products)

orders = {
     "Alice": ["Laptop", "Mouse"],
     "Bob": ["Keyboard"],
     "Charlie": ["Monitor", "Mouse", "Laptop"]
}

most_products = 0
best_customer = ""

for customer in orders:
    print(customer)
    products = orders[customer]
    print(products)

    total = count_products(products)
    print("Total products bought: ", total)

    if total > most_products:
        most_products = total
        best_customer = customer

print("Top customer:", best_customer)
print("Products:", most_products)