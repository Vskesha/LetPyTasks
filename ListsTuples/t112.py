string = input('Введи текст: ')
kword = input('Введи шукане слово: ').lower()
words = string.replace('.', ' ').replace(',', ' ').lower().split()
print(words.count(kword))