# Python Program to Find the Second Largest Number in a List Using Bubble Sort

li = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

for i in range(n - 1):
    for j in range(n - i - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("Sorted List:", li)
print("Second Largest Number:", li[-2])