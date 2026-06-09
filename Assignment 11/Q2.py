# Python Program to Merge Two Lists and Sort it

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

merged_list = list1 + list2
merged_list.sort()

print("List 1 :", list1)
print("List 2 :", list2)
print("Merged and Sorted List:", merged_list)