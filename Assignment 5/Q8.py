#a.
num = int(input('Enter num:'))
sum = 0
fact = 1

for i in range(1, num + 1):
    fact *= i
    sum += fact

print('sum of series:', sum)

#b.

num = int(input('Enter num:'))
sum = 0
for i in range(1, num + 1):
    sum += num **i
    
print('sum of series:', sum)

#c.

num = int(input('Enter numbers of terms:'))
sum = 0
terms = 1

for i in range(num):
    sum += terms
    terms *= 2
    
print('Sum of geometric series:', sum)

#d.

num = int(input('Enter num:'))
sum = 0
for i in range(1, 11):
    sum += num**i / i
    
print('sum of series:', sum)

#e.

x = int(input('Enter x:'))
n = int(input('Enter number of terms:'))
sum = 0

for i in range(1, n+1):
    term = (x**i) / (2*i - 1)
    if i % 2 == 0:
        term = -term
    sum += term

print('Sum of series:', sum)