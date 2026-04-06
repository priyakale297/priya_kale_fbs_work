total_amount = 0

for i in range(1, 6):
    print(f'\nPerson {i}:')
    age = int(input('Enter age: '))
    ticket = int(input('Enter ticket amount:'))

    if age < 12:
        amount_to_pay = ticket * 0.7 
    elif age > 59:
        amount_to_pay = ticket * 0.5  
    else:
        amount_to_pay = ticket        

    print(f'Amount to pay for person {i}: {amount_to_pay}')
    total_amount += amount_to_pay

print(f'\nTotal amount for all 5 people: {total_amount}')