import tkinter as tk
import time
import random

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

circles = []
colors = ('red', 'orange', 'yellow', 'green', 'cyan', 'purple')

for i in range(5):
    color = random.choice(colors)
    r = random.randint(5, 25)
    cx = random.randint(r, 400 - r)
    cy = random.randint(r, 400 - r)
    oval = canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color)
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    circles.append({'dx': dx, 'dy': dy, 'id': oval})

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])
        if x0 < 0 or x1 > 400:
            circle['dx'] = -circle['dx']
        if y0 < 0 or y1 > 400:
            circle['dy'] = -circle['dy']
        canvas.move(circle['id'], circle['dx'], circle['dy'])
    canvas.update()
    time.sleep(0.01)
window.mainloop()