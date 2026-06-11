# Function to remove nth index character
def remove_char(string, n):
    return string[:n] + string[n+1:]

text = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

if 0 <= n < len(text):
    result = remove_char(text, n)
    print("String after removing character:", result)
else:
    print("Invalid index!")