def chk_palindrome(num):
    original = num
    rev = 0

    for i in range(num):
        if num == 0:
            break

        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if original == rev:
        print('Palindrome Number')
    else:
        print('Not Palindrome Number')

num = int(input('Enter number:'))

chk_palindrome(num)