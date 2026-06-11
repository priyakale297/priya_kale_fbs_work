# Program to generate dictionary with numbers and their squares

n = int(input("Enter a number: "))

my_dict = {}

for x in range(1, n + 1):
    my_dict[x] = x * x

print("Generated Dictionary:", my_dict)