string = input('Введи текст: ')
words = string.replace('.', ' ').replace(',', ' ').lower().split()
wc = {}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
wl = list(wc.keys())
wl.sort()
for word in wl:
    print(f'{word}:{wc[word]}')