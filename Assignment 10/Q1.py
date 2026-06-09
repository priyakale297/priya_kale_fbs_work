# Program to find the sum of all elements in a list

lst = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

total = sum(lst)

print("List =", lst)
print("Sum of all elements:", total)