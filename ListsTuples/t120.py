string = input('Введи речення: ')
words = string.split()
for i, w in enumerate(words, 1):
    print(i, w)