# Program to count occurrences of each word in a string

string = input("Enter a string: ")

words = string.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word in word_count:
    print(word, ":", word_count[word])