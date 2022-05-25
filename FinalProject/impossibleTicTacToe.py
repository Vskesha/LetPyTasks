import tkinter, time, random


class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.colors = (('brown1', 'brown2', 'coral', 'coral3', 'OliveDrab1', 'orange red'),
                       ('cyan', 'cyan3', 'cornflower blue', 'DarkBlue', 'dark cyan', 'navy'))
        self.color_o = random.choice(self.colors[0])
        self.color_x = random.choice(self.colors[1])
        self.state = [None, None, None, None, None, None, None, None, None]
        self.free_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.corners = ((0, 1, 3), (1, 2, 5), (3, 6, 7), (5, 7, 8))
        self.wins = {'x': 0, 'o': 0, 'draw': 0}
        self.game_is_running = True
        self.win = None
        self.bind('<Button-1>', self.click)
        self.ready = True

    def add_x(self, column, row):
        x1, y1, x2, y2 = self.get_position(column, row)[0]
        x1, y2, x2, y1 = self.get_position(column, row)[1]
        self.create_line(x1, y1, x2, y2, width=5, fill=self.color_x)
        self.create_line(x1, y2, x2, y1, width=5, fill=self.color_x)
        self.update()

    def add_o(self, column, row):
        x1, y1, x2, y2 = self.get_position(column, row)[0]
        self.create_oval(x1, y1, x2, y2, width=5, outline=self.color_o)
        self.update()

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(0, 100, 300, 100, fill='grey')
        self.create_line(0, 200, 300, 200, fill='grey')
        self.update()

    def get_position(self, column, row):
        k = 10
        d = 100
        k2 = d - k
        x1, y1, x2, y2 = k + column * d, k + row * d, k2 + column * d, k2 + row * d
        cords = ((x1, y1, x2, y2), (x1, y2, x2, y1))
        return cords

    def click(self, event):
        if self.game_is_running is False and self.ready is True:
            self.new_game()
        elif self.game_is_running is True and self.ready is True:
            column = event.x // 100
            row = event.y // 100
            state_id = column + 3 * row
            if self.state[state_id] == None:
                self.state[state_id] = 'x'
                self.free_state.remove(state_id)
                self.add_x(column, row)
                if self.get_winner() is None: self.bot_move()

    def bot_move(self):
        if self.free_state:
            move_index = self.find_best()
            self.state[move_index] = 'o'
            column, row = move_index % 3, move_index // 3
            self.add_o(column, row)
            self.free_state.remove(move_index)
            self.get_winner()
        else:
            self.get_winner()

    def find_best(self):
        free_cross = []
        free_diag = []
        for i in (0, 2, 6, 8):
            if self.state[i] is None: free_diag.append(i)
        for i in (1, 3, 5, 7):
            if self.state[i] is None: free_cross.append(i)

        # Get WIN
        for i in range(3):
            x = (self.state[i], self.state[i + 3], self.state[i + 6])
            if None in x and x.count('o') == 2: return 3 * x.index(None) + i
        for i in (0, 3, 6):
            x = (self.state[i], self.state[i + 1], self.state[i + 2])
            if None in x and x.count('o') == 2: return x.index(None) + i
        for i in (2, 4):
            x = (self.state[4 - i], self.state[4], self.state[4 + i])
            if None in x and x.count('o') == 2: return 4 - i + x.index(None) * i
        # Don't let win
        for i in range(3):
            x = (self.state[i], self.state[i + 3], self.state[i + 6])
            if None in x and x.count('x') == 2: return 3 * x.index(None) + i
        for i in (0, 3, 6):
            x = (self.state[i], self.state[i + 1], self.state[i + 2])
            if None in x and x.count('x') == 2: return x.index(None) + i
        for i in (2, 4):
            x = (self.state[4 - i], self.state[4], self.state[4 + i])
            if None in x and x.count('x') == 2: return 4 - i + x.index(None) * i
            # ANY OTHER TURN EXEPT OF 4 IF IT IS FREE COULD LEAD TO X WIN
        if self.state[4] is None: return 4

        for i in (2, 4):
            x = (self.state[4 - i], self.state[4], self.state[4 + i])
            if self.state[4] == 'o' and x.count('x') == 2 and free_cross: return random.choice(free_cross)
            if self.state[4] == 'o' and x.count('x') == 1:
                if self.state[4 - i] is None:
                    return 4 - i
                elif self.state[4 + i] is None:
                    return 4 + i
            if self.state[4] == 'x' and free_diag: return random.choice(free_diag)

        for i in self.corners:
            x = (self.state[i[0]], self.state[i[1]], self.state[i[2]])
            if x.count('x') == 2 and None in x: return i[x.index(None)]

        if self.free_state:
            return random.choice(self.free_state)

    def get_winner(self):
        for i in range(3):
            if self.state[i] == self.state[i + 3] and self.state[i] == self.state[i + 6] and self.state[i] is not None:
                self.win = self.state[i]
                start_i, end_i = i, i + 6
                self.create_line((start_i % 3) * 100 + 50, (start_i // 3) * 100 + 10, (end_i % 3) * 100 + 50,
                                 (end_i // 3) * 100 + 90, width=10, fill='black')
                self.update()
        for i in (0, 3, 6):
            if self.state[i] == self.state[i + 1] and self.state[i] == self.state[i + 2] and self.state[i] is not None:
                self.win = self.state[i]
                start_i, end_i = i, i + 2
                self.create_line((start_i % 3) * 100 + 10, (start_i // 3) * 100 + 50, (end_i % 3) * 100 + 90,
                                 (end_i // 3) * 100 + 50, width=10, fill='black')
                self.update()
        for i in (2, 4):
            if self.state[4] == self.state[4 - i] and self.state[4] == self.state[4 + i] and self.state[i] is not None:
                self.win = self.state[i]
                if i == 2:
                    self.create_line(290, 10, 10, 290, width=13, fill='black')
                else:
                    self.create_line(10, 10, 290, 290, width=13, fill='black')
                self.update()
        if self.win is None:
            if None in self.state:
                return None
            else:
                self.wins['draw'] += 1
                self.end_game()
                return 'draw'
        else:
            self.wins[self.win] += 1
            self.end_game()
            return '{}_win'.format(self.win)

    def end_game(self):
        self.ready = False
        time.sleep(1)
        self.delete("all")
        if self.win is None:
            self.create_text(150, 150, text=f"Draw!", font=("Arial", 60))
            self.update()
        else:
            self.create_text(150, 150, text=f"{self.win.upper()} wins!", font=("Arial", 60))
            self.update()
        time.sleep(1)
        self.game_is_running = False
        # WINNERS
        self.delete("all")
        self.create_text(150, 150,
                         text=f"X wins - {self.wins['x']}\nO wins - {self.wins['o']}\nDraws  - {self.wins['draw']} ",
                         font=("Arial", 30))
        time.sleep(0.5)
        self.create_text(150, 270, text=f"Click to start new game", font=("Arial", 15))
        self.ready = True

    def new_game(self):
        self.delete("all")
        self.color_o = random.choice(self.colors[0])
        self.color_x = random.choice(self.colors[1])
        self.state = [None, None, None, None, None, None, None, None, None]
        self.free_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win = None
        self.draw_lines()
        self.game_is_running = True


window = tkinter.Tk()
window.title('TicTacToe')
game = TicTacToe(window)
game.pack()
game.draw_lines()
window.mainloop()