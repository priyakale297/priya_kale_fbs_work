def count_digits(num):
    count = 0
    for _ in range(num):
        count += 1
        num = num // 10
        if num == 0:
            break
    return count


def power(base, exp):
    result = 1
    for _ in range(exp):
        result = result * base
    return result


def is_armstrong(num):
    original = num
    digits = count_digits(num)

    total = 0

    for _ in range(num):
        if num == 0:
            break

        digit = num % 10
        total = total + power(digit, digits)
        num = num // 10

    if total == original:
        print('Armstrong Number')
    else:
        print('Not Armstrong Number')


num = int(input('Enter number:'))
is_armstrong(num)
     