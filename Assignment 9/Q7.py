# Program to find the sum of digits using recursion

def sum_of_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_of_digits(num // 10)

n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))