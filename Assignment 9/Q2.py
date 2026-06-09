# Program to check whether a number is Armstrong or not
# using a recursive function

def armstrong(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + armstrong(num // 10, power)

n = int(input("Enter a number: "))
digits = len(str(n))

if n == armstrong(n, digits):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")