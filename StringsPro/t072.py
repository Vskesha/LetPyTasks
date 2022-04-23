string = input('Введи текст: ')
if len(string) >= 2:
    print(string[0], string[-1])
else:
    print('Ошибка')