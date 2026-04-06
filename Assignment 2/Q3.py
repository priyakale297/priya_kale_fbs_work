feet = int(input('Enter distance in feet:'))
inches = int(input('Enter distance in inches:'))

total_inches = feet * 12 + inches

centimeters = total_inches * 2.54

meters = centimeters / 100

print('Distance in meters:', meters)
print('Distance in centimeters:', centimeters)