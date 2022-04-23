a = input('Введи перше число: ')
b = input('Введи друге число: ')
if a.isdigit() and b.isdigit():
    summ = int(a) + int(b)
    print('Сумма=' + str(summ))
else:
    print('Ошибка')