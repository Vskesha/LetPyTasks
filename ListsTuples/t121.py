import tkinter as tk
import random
import time

w = tk.Tk()
canv = tk.Canvas(w, width=400, height=400)
canv.pack()
colors = ('red', 'orange', 'yellow', 'green', 'cyan', 'dark blue', 'purple')
while True:
    cx = random.randint(0, 400)
    cy = random.randint(0, 400)
    for i, r in enumerate(range(150, 185, 5)):
        canv.create_oval(cx - r, cy - r, cx + r, cy + r, outline=colors[i])
        canv.update()
        time.sleep(0.05)