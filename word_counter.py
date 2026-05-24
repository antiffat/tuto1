# create a function that:
# receives text
# counts words
# prints occurrences

def count_words(text):
    words = text.lower().split()

    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    for word in counts:
        print(word, "->", counts[word])

text = input("enter text: ")
count_words(text)