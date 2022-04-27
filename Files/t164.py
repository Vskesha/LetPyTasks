catalog = {}
with open('t164.txt', 'r') as f:
    for line in f:
        name, count = line.split(':')
        catalog[name] = int(count)
        
for i in range(3):
    name = input('Введи назву товару: ')
    count = int(input('Введи його кількість: '))
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count
with open('t164.txt', 'w') as f:
    for k, v in catalog.items():
        f.write(f'{k}:{v}\n')