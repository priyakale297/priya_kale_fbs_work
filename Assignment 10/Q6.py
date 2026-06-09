# Program to remove duplicates from a list

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

new_list = list(set(li))

print("Original List =", li)
print("List after removing duplicates =", new_list)