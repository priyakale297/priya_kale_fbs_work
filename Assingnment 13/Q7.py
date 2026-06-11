# Program to remove a key from a dictionary

my_dict = {"name": "Priya", "age": 23, "city": "Pune"}

print("Original dictionary:", my_dict)

key = input("Enter key to remove: ")

if key in my_dict:
    del my_dict[key]
    print("Key removed successfully")
else:
    print("Key not found in dictionary")

print("Updated dictionary:", my_dict)