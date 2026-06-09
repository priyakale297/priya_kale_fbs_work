# Program to create a duplicate (copy) of an existing list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

copy_list = li.copy()

print("Original List =", li)
print("Duplicate List =", copy_list)