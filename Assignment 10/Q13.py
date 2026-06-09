# Program to print a list after removing even numbers

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

new_list = []

for i in li:
    if i % 2 != 0:
        new_list.append(i)

print("Original List =", li)
print("List after removing even numbers:", new_list)