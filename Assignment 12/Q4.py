# Program to exchange the first and last characters of a string

string = input("Enter a string: ")

if len(string) <= 1:
    new_string = string
else:
    new_string = string[-1] + string[1:-1] + string[0]

print("New string:", new_string)