n = int(input('Enter value of n:'))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact *= i
    sum += i / fact

print('Sum of series:', sum)