class TicTacToe():
    @staticmethod
    def checkLineForWinner(line):
        line = tuple(line)
        winner_states = {
            ('O', 'O', 'O'): -1,
            ('X', 'X', 'X'): 1,
        }

        if line not in winner_states:
            return 0

        return winner_states[line]


    @staticmethod
    def checkForTie(board):
        for i in range(len(board)):
            if isinstance(board[i], int):
                return False
            else:
                continue
        return True

        

    @staticmethod
    def checkForVerticalWin(board):
        temp_line = []
        for i in range(3):
            for j in range(3):
                temp_line.append(board[i + j*3])
                winner = TicTacToe.checkLineForWinner(temp_line)
                if winner == 1 or winner == -1:
                    return winner
        return winner
                    
    @staticmethod
    def checkForHorizontalWin(board):
        temp_line = []
        for i in range(3):
            for j in range(3):
                temp_line.append(board[i*3 + j])
            winner = TicTacToe.checkLineForWinner(temp_line)
            if winner == 1 or winner == -1:
                return winner
            temp_line = []
        return winner

    @staticmethod
    def checkForDiagnolWin(board):
        diagnols = [[board[0], board[4], board[8]], [board[2], board[4],board[6]]]
        for diagnol in diagnols:
            winner = TicTacToe.checkLineForWinner(diagnol)
            if winner == 1 or winner == -1:
                return winner
        return winner

    