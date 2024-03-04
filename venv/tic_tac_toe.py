import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text="", font=('normal', 40), height=2, width=5,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner() and not self.check_tie():
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":  # AI's turn
                    self.ai_move()

    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        if winner:
            return 1 if winner == "O" else -1
        
        if self.check_tie():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == "":
                        self.board[row][col] = "O"  # AI makes a move
                        score = self.minimax(depth + 1, False)
                        self.board[row][col] = ""  # Undo the move
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == "":
                        self.board[row][col] = "X"  # Player's move
                        score = self.minimax(depth + 1, True)
                        self.board[row][col] = ""  # Undo the move
                        best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.board[row][col] = "O"  # AI makes a move
                    score = self.minimax(0, False)
                    self.board[row][col] = ""  # Undo the move
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        if best_move:
            self.buttons[best_move[0]][best_move[1]].config(text="O")
            self.board[best_move[0]][best_move[1]] = "O"
            winner = self.check_winner()  # Check if the AI's move wins the game
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_board()
            elif self.check_tie():  # Check if the game is a tie
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "X"  # Switch back to the player

    def check_winner(self):
        for symbol in ["X", "O"]:
            for i in range(3):
                if all(self.board[i][col] == symbol for col in range(3)) or all(self.board[row][i] == symbol for row in range(3)):
                    return symbol
                if (self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol) or (self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol):
                    return symbol
        return None

    def check_tie(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
                self.board[row][col] = ""
        self.current_player = "X"

    def start_game(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
