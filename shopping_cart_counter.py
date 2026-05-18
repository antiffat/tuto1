# task 2
# A store wants to know how many times each product was bought.
# You are given:
# products = [
# "apple",
# "banana",
# "apple",
# "orange",
# "banana",
# "apple"
# ]
# count how many times each product appears.
# apple: 3
# banana: 2
# orange: 1

products = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]

counts = {}
# counts = { "apple": 1 }
# counts = { "apple": 2, "banana": 2 }

for product in products:
    if product not in counts:
        counts[product] = 1
        # counts["apple"] = 1
        # counts["banana"] = 1
    else:
        counts[product] += 1
        #counts["apple"] += 1

print(counts)