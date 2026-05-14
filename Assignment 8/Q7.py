def sum_of_digit(n):
    total = 0

    for digit in str(n):
        total += int(digit)

    return total
n = int(input('Enter number:'))
print('sum of digits of a number:', sum_of_digit(n)) 