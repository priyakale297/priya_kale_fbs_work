def calculate_area(length, width):
    area = length * width
    return area

length = int(input('Enter Length:'))
width = int(input('Enter Width:'))
    
area = calculate_area(length, width)

print('The area of the rectangle is:',area)