n = int(input('Enter number of passengers:'))
cost = float(input('Enter ticket cost:'))

total_amount = 0

for i in range(n):
    age = int(input(f'Enter age of passenger {i+1}:'))

    if age < 12:
        price = cost - (cost * 0.30)   
    elif age > 59:
        price = cost - (cost * 0.50)  
    else:
        price = cost                

    total_amount += price

print('Total amount to pay =', total_amount)