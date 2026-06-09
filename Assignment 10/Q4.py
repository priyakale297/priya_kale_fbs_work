# Program to reverse a list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

li.reverse()

print("Reversed List:", li)