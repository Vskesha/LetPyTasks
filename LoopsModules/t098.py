import tkinter as tk
import time

w = tk.Tk()
c = tk.Canvas(w)
c.pack()
r = c.create_rectangle(0, 50, 100, 150)
x = 0
dx = 2
while True:
    c.coords(r, x, 50, x + 100, 150)
    c.update()
    time.sleep(0.01)
    if x > 200 or x < 0:
        dx = -dx
    x += dx
w.mainloop()