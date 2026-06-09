# Program to find the second largest element in a list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

li.sort()

print("List:", li)
print("Second largest element:", li[-2])