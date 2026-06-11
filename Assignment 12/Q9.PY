# Program to count words and characters in a string

string = input("Enter a string: ")

char_count = len(string)

words = string.split()
word_count = len(words)

print("Number of words:", word_count)
print("Number of characters:", char_count)