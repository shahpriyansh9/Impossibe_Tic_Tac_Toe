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