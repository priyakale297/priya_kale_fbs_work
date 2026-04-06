cost_price = int(input('Enter cost price of the book:'))
discount = int(input('Enter discount percentage:'))

discount_amount = (cost_price * discount) / 100

selling_price = cost_price - discount_amount

print('Selling Price of the book:', selling_price)