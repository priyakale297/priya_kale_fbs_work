# Program to create a new list containing the cube of each element of an existing list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

cube_list = []

for i in li:
    cube_list.append(i ** 3)

print("Original List:", li)
print("Cube List:", cube_list)