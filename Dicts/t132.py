catalog = {}
for i in range(3):
    name = input('Введи назву товару: ')
    count = int(input('Його кількість: '))
    catalog[name] = count
for k, v in catalog.items():
    print(f'{k}:{v}')