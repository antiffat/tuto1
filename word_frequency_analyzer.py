# Ask the user for a sentence.
#
# Count how many times each word appears.
#
# Example:
# Input:
# cat dog cat bird dog cat
#
# Output:
# cat -> 3
# dog -> 2
# bird -> 1
from shopping_cart_counter import counts

# text = "word cat dog"
# words = text.split()
# print(words)

sentence = input("Enter sentence: ")

words = sentence.lower().split()

counts = {}

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

for word in counts:
    print(word, "->", counts[word])