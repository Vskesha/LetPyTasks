import json

with open('t173.json', 'r') as file:
    catalog = json.loads(file.read())

for i in range(3):
    name = input('Введи назву товару: ')
    count = int(input('Введи його кількість: '))
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count

with open('t173.json', 'w') as f:
    f.write(json.dumps(catalog, ensure_ascii=False))