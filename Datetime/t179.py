import datetime as dt

try:
    date_str = input('Введи дату и время в формате ДД/ММ/ГГГГ ЧЧ:ММ:CC ')
    my_datetime = dt.datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
except ValueError:
    print('Ошибка')