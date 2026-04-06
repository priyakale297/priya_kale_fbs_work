uid = 'admin'
pwd = '123'

for i in range(3):
    user = input('Enter user id:')
    password = input('Enter password:')

    if user == uid and password == pwd:
        print('Login successful')
        break
    else:
        print('Wrong id or password')

else:
    print('Program terminated after 3 attempts')