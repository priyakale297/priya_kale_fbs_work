P = int(input('Enter Principal amount:'))
T = int(input('Enter the Time:'))
R = int(input('Enter Rate of interest:'))

A = P * (1 + R/100) ** T
CI = A - P

print('Compound Interest:', CI)