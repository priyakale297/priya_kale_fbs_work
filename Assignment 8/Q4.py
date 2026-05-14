def sum_odd(n):
    total = 0
    for i in range(1, n + 1, 2): 
            total += i
    return total

n = int(input('Enter number:'))
print('Sum of all odd numbers:',sum_odd(n)) 