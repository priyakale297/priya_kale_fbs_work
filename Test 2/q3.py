while True:
    r = 20
    l = 50
    b = 40
    cost_per_m = 35

    semi = 3.14 * r + 2 * r

    rect = 2 * (l + b)

    total = semi + rect

    wire = total * 5

    cost = wire * cost_per_m

    print('Total cost of fencing:', cost)
    break
   
        