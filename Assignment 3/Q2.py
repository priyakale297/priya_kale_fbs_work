ch = input('Enter an alphabet:')

if ch.isalpha():                    
    ch = ch.lower()                  
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print('It is a Vowel')
    else:
        print('It is a Consonant')
else:
    print('Invalid input! Please enter an alphabet.')