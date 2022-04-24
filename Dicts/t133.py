catalog = {}
for i in range(3):
    name = input('Введи назву товару: ')
    count = int(input('Його кількість: '))
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count
for k, v in catalog.items():
    print(f'{k}:{v}')