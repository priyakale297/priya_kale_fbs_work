num = int(input('Enter a number:'))

temp = num

count = 0
while temp > 0:
    count += 1
    temp //= 10

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    
    power = 1
    for i in range(count):
        power *= digit
    
    sum += power
    temp //= 10

if sum == num:
    print(num, 'is an Armstrong Number')
else:
    print(num, 'is NOT an Armstrong Number')