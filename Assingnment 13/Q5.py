# Program to sum all values in a dictionary

my_dict = {"a": 10, "b": 20, "c": 30, "d": 40}

total = 0

for key in my_dict:
    total += my_dict[key]

print("Sum of all items in dictionary:", total)