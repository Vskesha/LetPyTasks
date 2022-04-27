import csv

catalog = {}
with open('t168.csv', 'r') as f:
    for name, count in csv.reader(f):
        catalog[name] = int(count)
        
for i in range(3):
    name = input('Введи назву товару: ')
    count = int(input('Введи його кількість: '))
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count
with open('t168.csv', 'w') as f:
    writer = csv.writer(f)
    for row in catalog.items():
        writer.writerow(row)
        