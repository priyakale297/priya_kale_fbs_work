def sum_natural(n):
    total  = 0
    for i in range(1, n + 1):
        total += i
    return total

def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_fact(n):
    total = 0
    for i in range(1, n + 1):
        total += fact(i)
    return total

def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input('Enter the value n:'))

print('Sum of 1 + 2 + ... + n:', sum_natural(n))
print('Sum of 1! + 2! + ... + n!:', sum_fact(n))
print('Sum of 1^1 + 2^2 + ... + n^n:', sum_power(n))
    