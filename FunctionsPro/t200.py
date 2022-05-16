import tkinter as tk
import random as rnd
import time

window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=400, background='yellow')
canvas.pack()

colors = ('red', 'orange', 'green', 'cyan', 'dark blue', 'purple', 'black', 'white', 'brown', 'grey20')

def my_click(ev):
	color = rnd.choice(colors)
	color2 = rnd.choice(colors)
	r = rnd.randint(20, 60)
	canvas.create_oval(ev.x - r, ev.y - r, ev.x + r, ev.y + r, outline=color, fill=color2)
	canvas.update()

canvas.bind('<Button-1>', my_click)
canvas.bind
window.mainloop()