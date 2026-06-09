# Program to find the sum of the series:
# 1! + 2! + 3! + ... + n!
# Using two recursive functions

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def series_sum(n):
    if n == 1:
        return fact(1)
    return fact(n) + series_sum(n - 1)


n = int(input("Enter the value of n: "))
print('Sum of the series:', series_sum(n))