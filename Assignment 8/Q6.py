def Fibonacci(n):
    a = 1
    b = 1
    
    for i in range(n):
        c = a + b
        print(a, end=' ')
        a = b
        b = c
Fibonacci(6)