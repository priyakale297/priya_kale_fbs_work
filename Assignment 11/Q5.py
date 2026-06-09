# Python Program to Sort a List According to the Length of the Elements

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    item = input("Enter element: ")
    li.append(item)

li.sort(key=len)

print("Sorted List:", li)