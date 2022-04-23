t = int(input('Введи температуру: '))
if t < -4:
    print('морозно')
elif t < 0:
    print('холодно')
elif t < 12:
    print('прохладно')
elif t < 27:
    print('тепло')
else:
    print('жарко')