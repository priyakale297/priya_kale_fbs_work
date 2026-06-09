# Program to find maximum and minimum element in a list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

maximum = max(li)
minimum = min(li)

print("List =", li)
print("Maximum element:", maximum)
print("Minimum element :", minimum)