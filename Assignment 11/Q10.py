# Program to remove even numbers from a list

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for i in li:
    if i % 2 != 0:
        result.append(i)

print("Original List:", li)
print("List after removing even numbers:", result)