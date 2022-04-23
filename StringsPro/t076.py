string = input('Введи слово або фразу: ').replace(' ', '').replace('.', '').replace(',', '').lower()
if string == string[::-1]:
    print('да')
else:
    print('нет')