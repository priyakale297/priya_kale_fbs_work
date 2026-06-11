# Program to count word frequency using dictionary

string = input("Enter a string:")

words = string.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
for word in freq:
    print(word, ":", freq[word])