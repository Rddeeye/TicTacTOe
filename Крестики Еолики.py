import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ход игрока X")
        self.player = 'X'
        self.board = [' ' for _ in range(9)]
        self.buttons = [None for _ in range(9)]
        self.create_buttons()
        self.bind_keys()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='Arial 20', width=8, height=3,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons[i] = button

    def bind_keys(self):
        self.root.bind('7', lambda event: self.make_move(0))
        self.root.bind('8', lambda event: self.make_move(1))
        self.root.bind('9', lambda event: self.make_move(2))
        self.root.bind('4', lambda event: self.make_move(3))
        self.root.bind('5', lambda event: self.make_move(4))
        self.root.bind('6', lambda event: self.make_move(5))
        self.root.bind('1', lambda event: self.make_move(6))
        self.root.bind('2', lambda event: self.make_move(7))
        self.root.bind('3', lambda event: self.make_move(8))

    def make_move(self, i):
        if self.board[i] == ' ':
            self.board[i] = self.player
            self.buttons[i].config(text=self.player)
            self.update_title()
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.player} выиграл!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Ничья!", "Игра окончена вничью!")
                self.reset_game()
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.update_title()

    def update_title(self):
        self.root.title(f"Ход игрока {self.player}")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтально
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикально
            [0, 4, 8], [2, 4, 6]  # по диагонали
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.player = 'X'
        for button in self.buttons:
            button.config(text=' ')
        self.update_title()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()