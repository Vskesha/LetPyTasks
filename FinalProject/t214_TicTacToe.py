import tkinter as tk
import random as rnd

class TicTacToe(tk.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.state = [None, None, None, None, None, None, None, None, None]
        self.bind('<Button-1>', self.click)

    def click(self, event):
        column = event.x // 100
        row = event.y // 100
        i = row * 3 + column
        if self.state[i] is None:
            self.state[i] = 'x'
            self.add_x(column, row)
            self.bot_move()

    def add_x(self, column, row):
        x = column * 100
        y = row * 100
        self.create_line(x + 10, y + 10, x + 90, y + 90, width=5, fill='dark blue')
        self.create_line(x + 90, y + 10, x + 10, y + 90, width=5, fill='dark blue')
    
    def add_o(self, column, row):
        x = column * 100
        y = row * 100
        self.create_oval(x + 10, y + 10, x + 90, y + 90, width=5, outline='red')
    
    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey20')
        self.create_line(200, 0, 200, 300, fill='grey20')
        self.create_line(0, 100, 300, 100, fill='grey20')
        self.create_line(0, 200, 300, 200, fill='grey20')

    def bot_move(self):
        empty_squares = []
        for i in range (len(self.state)):
            if self.state[i] is None:
                empty_squares.append(i)
        if empty_squares:
            i = rnd.choice(empty_squares)
        else:
            return
        self.state[i] = 'o'
        column = i % 3
        row = i // 3
        self.add_o(column, row)

    def get_winner(self):
        l = self.state
        win_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for i, j, k in win_combinations:
            if l[i] == 'x' and l[j] == 'x' and l[k] == 'x':
                return 'x_win'
            if l[i] == 'o' and l[j] == 'o' and l[k] == 'o':
                return 'o_win'
        if not None in l:
            return 'draw'




window = tk.Tk()
window.title('Хрестики-Нолики')
game = TicTacToe(window)
game.pack()
game.draw_lines()


window.mainloop()