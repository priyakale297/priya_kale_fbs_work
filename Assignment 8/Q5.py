def sum_prime(n):
    total = 0

    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            total += num

    return total
    
n = int(input('Enter number:'))

print('Sum of all prime number:',sum_prime(n))