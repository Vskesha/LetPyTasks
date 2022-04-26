def choose_plural (n, t):
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} {t[0]}'
    elif (2 <= n % 10 <= 4) and (n % 100 < 10 or n % 100 > 20):
        return f'{n} {t[1]}'
    else:
        return f'{n} {t[2]}'
