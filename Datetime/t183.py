import datetime as dt

def choose_plural (n, t):
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} {t[0]}'
    elif (2 <= n % 10 <= 4) and (n % 100 < 10 or n % 100 > 20):
        return f'{n} {t[1]}'
    else:
        return f'{n} {t[2]}'

try:
    date_x = dt.datetime.strptime(input('Введи дату в формате ДД.ММ.ГГГГ ЧЧ:ММ '), '%d.%m.%Y %H:%M')
    now = dt.datetime.now()
    if date_x < now:
        print('Ошибка')
    else:
        delta = date_x - now.replace(second=0, microsecond=0)
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds // 60) % 60
        sdays = choose_plural(days, ('день', 'дня', 'дней'))
        shours = choose_plural(hours, ('час', 'часа', 'часов'))
        sminutes = choose_plural(minutes, ('минута', 'минуты', 'минут'))
        if days:
            result = sdays + ((' и ' + shours) if hours else '')
        elif hours:
            result = shours + ((' и ' + sminutes) if minutes else '')
        else:
            result = sminutes
        print('До часа "Икс" ' + result)
except ValueError:
    print('Ошибка')