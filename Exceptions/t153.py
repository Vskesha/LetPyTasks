try:
    a = int(input('Введи перше число: '))
    b = int(input('Введи друге число: '))
    print(a + b)
except ValueError:
    print('Вы ввели не число')