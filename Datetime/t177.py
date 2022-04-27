import datetime as dt

my_datetime = dt.datetime.now()
str_date = my_datetime.strftime('%d %b\n%H:%M')
print(str_date)
