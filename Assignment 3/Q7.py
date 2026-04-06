correct_userid = 'admin'
correct_password = '12345'

userid = input('Enter User ID:')
password = input('Enter Password:')

if userid == correct_userid and password == correct_password:
    print('Login Successful')

elif userid != correct_userid:
    print('Incorrect User ID')

elif password != correct_password:
    print('Incorrect Password')

else:
    print('Login Failed')