num = int(input('How many fibonacci you want:'))
a = -1
b = 1
for i in range(num):
    c = a + b
    print(c)
    a = b
    b = c