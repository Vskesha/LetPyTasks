import random

number = random.randint(0, 10)
for i in range(3):
    n = int(input('Введи число: '))
    if number < n:
        print('Загаданное число меньше')
    elif number > n:
        print('Загаданное число больше')
    else:
        print('Вы выиграли')
        break
else:
    print('Вы проиграли')