import tkinter as tk

w = tk.Tk()
canv = tk.Canvas(w)
canv.pack()
for i in range(5, 100, 5):
    color = 'grey' if i%2 else 'red'
    canv.create_oval(150 - i, 100 - i, 150 + i, 100 + i, outline=color)
canv.update()
w.mainloop()