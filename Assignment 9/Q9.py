# Program to calculate m raised to the power n using recursion

def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

m = int(input("Enter the base (m): "))
n = int(input("Enter the exponent (n): "))

print("Result:", power(m, n))