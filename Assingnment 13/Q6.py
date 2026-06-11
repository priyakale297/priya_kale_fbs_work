# Program to multiply all values in a dictionary

my_dict = {"a": 2, "b": 3, "c": 4, "d": 5}

product = 1

for key in my_dict:
    product *= my_dict[key]

print("Product of all items in dictionary:", product)