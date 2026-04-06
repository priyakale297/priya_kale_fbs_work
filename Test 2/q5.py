while True:
    total = 0

    for i in range(5):
        price = float(input('Enter price of product: '))
        total = total + price

    gst = total * 0.18
    bill = total + gst

    print('Total bill with GST:', bill)
    break