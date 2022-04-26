try:
    f = open('t158.txt')
    text = f.read()
    print(text)
except FileNotFoundError:
    print('Файл не знайдено')