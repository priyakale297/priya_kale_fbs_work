# Python Program to Sort the List
# According to the Second Element in Sublist

li = []

n = int(input("Enter the number of sublists: "))

for i in range(n):
    a = int(input("Enter first element: "))
    b = int(input("Enter second element: "))
    li.append([a, b])

li.sort(key=lambda x: x[1])

print("Sorted List:", li)