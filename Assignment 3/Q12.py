num = input('Enter a 3-digit number:')

if len(num) == 3 and num.isdigit():
    if num == num[::-1]:
        print(f'{num} is a palindrome')
    else:
        print(f'{num} is not a palindrome')
else:
    print('Please enter a valid 3-digit number')