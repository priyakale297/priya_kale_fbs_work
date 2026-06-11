# Program to count lowercase characters in a string

string = input("Enter a string: ")

count = 0

for char in string:
    if char.islower():
        count += 1

print("Number of lowercase characters:", count)