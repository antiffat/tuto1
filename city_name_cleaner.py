# cities = [" Warsaw", "gdansk ", " WroCLAW", "kraków", " POZNAN "]
# Create a program that:
# Goes through every city
# Removes spaces at the beginning/end
# Converts the name to lowercase
# Stores cleaned cities in a NEW list
# Prints the cleaned list
# ['warsaw', 'gdansk', 'wroclaw', 'kraków', 'poznan']

cities = [" Warsaw", "gdansk ", " WroCLAW", "kraków", " POZNAN "]
cleaned_list = []

for city in cities:
    cleaned_list.append(city.strip().lower())

print(cleaned_list)