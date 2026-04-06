beg = int(input('Enter begining of range:'))
end = int(input('Enter ending of range:'))
for num in range(beg, end + 1):
    if (num % 7 == 0 and num % 5 == 0):
          print(num)