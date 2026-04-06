a = int(input('Enter value of a:'))
b = int(input('Enter value of b:'))
c = int(input('Enter value of c:'))

d = (b**2 - (4*a*c))**0.5

r1 = (-b+d)/2*a
r2 = (-b-d)/2*a


print('Root 1:', r1)
print('Root 2:', r2)