from itertools import product
import string

# Finding max and min length of words
min_len = int(input("Enter minimum length of password: "))
max_len = int(input("Enter maximum length of password: "))

# Count how many words
counter = 0

# Characters for generating words
character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

# Creating file and write the generated words
file_open = open("wordlist.txt", 'w')

# Shuffle the words
for i in range(min_len, max_len+1):
    for j in product(character, repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter += 1

print("Wordlist of {} passwords created".format(counter))