n = int(input('Enter number of employees:'))
grand = 0

for i in range(1, n + 1):
    basic = float(input(f'\nEnter basic salary of employee {i}:'))

    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total = basic + da + ta + hra
    grand += total

    print(f'Total salary of employee {i} = {total:.2f}')

print(f'\nTotal salary of all employees = {grand:.2f}')