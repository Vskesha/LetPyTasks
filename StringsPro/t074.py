string = input('Введи текст: ')
if len(string) >= 5:
    print(string[:3], string[-3:])
else:
    print('Ошибка')