catalog = {}
for i in range(3):
    name = input('Введи назву товару: ')
    count = int(input('Введи його кількість: '))
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count
with open('t163.txt', 'w') as f:
    for k, v in catalog.items():
        f.write(f'{k}:{v}\n')