s = input('Введи № тел. (мін 8 цифр): ')
if len(s) >=8 and s.isdigit():
    print('*' * (len(s) - 4) + s[-4:])
else:
    print('Ошибка')