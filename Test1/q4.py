area_one_wall = int(input('Enter area of one wall (in sq. units): '))
interior_cost_per_unit = int(input('Enter interior painting cost per sq. unit: '))
exterior_cost_per_unit = int(input('Enter exterior painting cost per sq. unit: '))

total_walls = 8

total_area = area_one_wall * total_walls

interior_cost = total_area * interior_cost_per_unit
exterior_cost = total_area * exterior_cost_per_unit

total_cost = interior_cost + exterior_cost

print('Total wall area:', total_area)
print('Interior painting cost:', interior_cost)
print('Exterior painting cost:', exterior_cost)
print('Total painting cost:', total_cost)