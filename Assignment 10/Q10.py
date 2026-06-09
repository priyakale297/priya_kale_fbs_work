# Program to remove all occurrences of a given element from a list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

x = int(input("Enter the element to remove: "))

while x in li:
    li.remove(x)

print("List after removing all occurrences:", li)