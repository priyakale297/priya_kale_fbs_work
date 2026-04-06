import random

correct_userid = 'admin'
correct_password = '12345'

userid = input('Enter User ID:')
password = input('Enter Password:')

if userid == correct_userid and password == correct_password:
    print('Login Successful!')

    captcha = random.randint(1000, 9999)
    print('Captcha:', captcha)

    user_captcha = int(input('Enter the captcha number shown above:'))

    if user_captcha == captcha:
        print('Verification Successful!')
    else:
        print('Verification Failed! Captcha does not match.')

else:
    print('Invalid User ID or Password.')