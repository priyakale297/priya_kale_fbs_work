# Program to create three lists:
# 1. Numbers
# 2. Squares of numbers
# 3. Cubes of numbers

numbers = []
squares = []
cubes = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
    squares.append(num ** 2)
    cubes.append(num ** 3)

print("Numbers List:", numbers)
print("Squares List:", squares)
print("Cubes List:", cubes)