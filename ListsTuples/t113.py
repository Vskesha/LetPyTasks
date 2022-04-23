string = input('Введи речення з цифрами: ')
words = string.split()
numbers = []
for word in words:
    if word.isdigit():
        numbers.append(int(word))
numbers.sort()
print(numbers)