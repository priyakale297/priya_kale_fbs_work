# Program to print all numbers divisible by both m and n in a list

li = []

size = int(input("Enter the number of elements: "))

for i in range(size):
    num = int(input("Enter element: "))
    li.append(num)

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("Numbers divisible by", m, "and", n, "are:")

for i in li:
    if i % m == 0 and i % n == 0:
        print(i, end=" ")