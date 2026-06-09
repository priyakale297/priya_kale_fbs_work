# Program to reverse a number using a recursive function

rev = 0

def reverse(num):
    global rev
    if num == 0:
        return
    digit = num % 10
    rev = rev * 10 + digit
    reverse(num // 10)


n = int(input("Enter a number: "))
reverse(n)

print("Reversed number:", rev)