string = input('Введи речення: ')
words = string.split()
rstring = ' '.join(words[::-1])
print(rstring)