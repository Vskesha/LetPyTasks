import tkinter as tk

w = tk.Tk()
canv = tk.Canvas(w)
canv.pack()
canv.create_rectangle(20, 20, 100, 100)
canv.create_rectangle(40, 40, 80, 80)
w.mainloop()