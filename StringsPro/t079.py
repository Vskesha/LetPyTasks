string = input('Введи текст: ')
if '#' in string:
    print(string[:string.find('#')])
else:
    print(string)