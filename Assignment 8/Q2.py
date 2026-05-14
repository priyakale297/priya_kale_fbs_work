def cal_circle_area(r):
    area = 3.14 * r ** 2
    return area

r = int(input('Enter the radius of circle:'))
area = cal_circle_area(r)
print('The area of circle is', area)
    