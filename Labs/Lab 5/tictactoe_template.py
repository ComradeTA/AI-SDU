from tictactoe_helper_functions import TicTacToe

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state, 'X'):
            v = max(v, min_value(s))
        #print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state, 'O'):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state, 'X'), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    winner = TicTacToe.checkForDiagnolWin(state)
    if winner != 0:
        return True
    winner = TicTacToe.checkForHorizontalWin(state)
    if winner != 0:
        return True
    winner = TicTacToe.checkForVerticalWin(state)
    if winner != 0:
        return True
    return TicTacToe.checkForTie(state)



def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    winner = TicTacToe.checkForDiagnolWin(state)
    if winner != 0:
        return winner
    winner = TicTacToe.checkForHorizontalWin(state)
    if winner != 0:
        return winner
    winner = TicTacToe.checkForVerticalWin(state)
    if winner != 0:
        return winner
    if TicTacToe.checkForTie(state) == True:
        return 0


def successors_of(state, player):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    moves = []
    temp_state = state.copy()
    for i in range(len(state)):
        if isinstance(state[i],int):
            temp_state[i] = player
            moves.append((i, temp_state))
            temp_state = state.copy()
        else:
            continue
    #print(moves)
    return moves


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)

def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
