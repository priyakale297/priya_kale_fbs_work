# Program to count vowels in a string

string = input("Enter a string: ")

count = 0
vowels = "priyakale"

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)