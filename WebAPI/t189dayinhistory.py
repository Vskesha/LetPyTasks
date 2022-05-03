import requests
import datetime as dt
import tkinter
import random

now = dt.datetime.now()
now = dt.datetime(2020, random.randint(1, 12), random.randint(1, 30))
date = now.strftime('%m/%d')

requests_count = 20
win_width = 1200
win_height = 700
win_font_size = 16
win_font = 'Verdana'
color = 'black'

events = {}
for i in range(requests_count):
    result = requests.get(f'http://numbersapi.com/{date}/date').text
    print(result)
    index_y = 20
    for l in result[20:]:
        if l.isdigit():
            break
        else:
            index_y += 1
    year = int(result[index_y:(index_y + 4)])
    event = result[((index_y + 10) if year >= 1000 else (index_y + 9)):]
    events[year] = event
years = list(events.keys())
years.sort()
win_text = f'{now.strftime("%d %B").upper()} IN HISTORY:\n\n'
for year in years:
    win_text += f'    {str(year).rjust(5)} -- {events[year]}\n'
print(win_text)
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=win_width, height=win_height)
canvas.pack()
canvas.create_text(0, 0, anchor=tkinter.NW, text=win_text, font=(win_font, win_font_size), fill=color, width=(win_width - 50))
canvas.update()
window.mainloop()