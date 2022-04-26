def factorial(n):
    f = 1
    for i in range (1, n + 1):
        f *= i
    print(f)
    
a = int(input('Введи число: '))
factorial(a)