# Program to concatenate two dictionaries

dict1 = {"name": "Priya", "age": 23}
dict2 = {"city": "Pune", "country": "India"}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

dict3 = dict1.copy()
dict3.update(dict2)

print("Concatenated Dictionary:", dict3)