def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong_number(num):
    temp = num
    sum_fact = 0

    while temp > 0:
        digit = temp % 10
        sum_fact += factorial(digit)
        temp //= 10

    return sum_fact == num

number = int(input('Enter a number:'))

if is_strong_number(number):
    print(number, 'is a Strong Number')
else:
    print(number, 'is NOT a Strong Number')