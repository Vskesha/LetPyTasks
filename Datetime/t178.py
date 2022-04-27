import tkinter as tk
import datetime as dt
import time

window = tk.Tk()
canvas = tk.Canvas(window, width=1200, height=500, bg='yellow')
canvas.pack()

timer = canvas.create_text(600, 250, text='', fill='dark blue', font=('Times New Roman', 250))
while True:
    time_now = dt.datetime.now()
    time_str = time_now.strftime('%H:%M:%S')
    canvas.itemconfig(timer, text=time_str)
    canvas.update()
    time.sleep(0.1)