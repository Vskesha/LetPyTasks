import tkinter as tk
import time

w = tk.Tk()
c = tk.Canvas(w)
c.pack()
r = c.create_rectangle(0, 50, 50, 100)
x = 0
while x < 200:
    c.coords(r, x, 50, x + 50, 100)
    c.update()
    time.sleep(0.01)
    x += 2
w.mainloop()