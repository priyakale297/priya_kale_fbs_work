# Program to check whether an element is present in the list
# and count its occurrences

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

x = int(input("Enter the element to search: "))

if x in li:
    print(x, "is present in the list.")
    print("It occurs", li.count(x), "time(s).")
else:
    print(x, "is not present in the list.")