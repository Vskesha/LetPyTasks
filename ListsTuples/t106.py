string = input('Введи текст: ')
words = string.split()
lword = ''
for word in words:
    if len(word) > len(lword):
        lword = word
print(lword)