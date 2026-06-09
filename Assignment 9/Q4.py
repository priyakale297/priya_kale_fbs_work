# Program to find the sum of first n natural numbers using recursion

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

n = int(input("Enter the value of n: "))
print("Sum:lo", find_sum(n))