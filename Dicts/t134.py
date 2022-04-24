string = input('Введи текст: ')
words = string.replace('.', ' ').replace(',', ' ').lower().split()
wc = {}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
for word, count in wc.items():
    print(f'{word}:{count}')