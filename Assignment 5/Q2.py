n = int(input('Enter number of students:'))

total_per = 0

for i in range(n):
    print('\nStudent', i+1)

    total_marks = 0
    for j in range(5):
        marks = int(input(f'Enter marks of subject {j+1}:'))
        total_marks += marks

    percentage = total_marks / 5
    print('Percentage =', percentage)

    total_per += percentage

avg = total_per / n
print('\nAverage percentage of all students =', avg)