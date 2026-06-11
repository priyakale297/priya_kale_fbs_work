# Program to check if a key exists in a dictionary

my_dict = {"name": "Priya", "age": 23, "city": "Pune"}

key = input("Enter key to search: ")

if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")