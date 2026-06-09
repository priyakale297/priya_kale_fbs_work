# Program to separate even and odd elements into two lists

li = []
even_list = []
odd_list = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

for i in li:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Original List:", li)
print("Even List:", even_list)
print("Odd List:", odd_list)