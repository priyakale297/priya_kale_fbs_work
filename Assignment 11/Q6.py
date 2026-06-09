# Python Program to Find the Union of Two Lists

list1 = []
list2 = []

n1 = int(input("Enter the number of elements in List 1: "))

for i in range(n1):
    num = int(input("Enter element: "))
    list1.append(num)

n2 = int(input("Enter the number of elements in List 2: "))

for i in range(n2):
    num = int(input("Enter element: "))
    list2.append(num)

union_list = list(set(list1 + list2))

print("List 1 :", list1)
print("List 2 :", list2)
print("Union of the two lists :", union_list)