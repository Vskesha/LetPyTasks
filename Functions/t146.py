def factorial(n):
    f = 1
    for i in range (1, n + 1):
        f *= i
    return f
    
a = int(input('Введи число: '))
print(factorial(a))