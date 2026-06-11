# Program to find the larger string without using built-in functions

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

len1 = 0
for ch in str1:
    len1 += 1

len2 = 0
for ch in str2:
    len2 += 1

if len1 > len2:
    print("Larger string:", str1)
elif len2 > len1:
    print("Larger string:", str2)
else:
    print("Both strings are of equal length")