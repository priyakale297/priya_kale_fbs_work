while True:
    l = int(input('Enter length of wall:'))
    h = int(input('Enter height of wall:'))
    cost = int(input('Enter cost per sq.m:'))

    area = 4 * l * h
    total_cost = area * cost

    print('Total cost:', total_cost)

    break