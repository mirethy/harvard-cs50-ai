"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0

    for row in board:
        xcount += row.count(X)
        ocount += row.count(O)
        
    if xcount <= ocount:
        return X
    else:
        return O

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == None:
                moves.add((i, j))

    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception('Invalid Action!')
    else:
        new_board[i][j] = player_move

    return new_board

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == X:
                return X
            elif board[row][0] == O:
                return O

#horizontal
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            if board[0][column] == X:
                return X
            elif board[0][column] == O:
                return O

#diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O

    if board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O

    return None
                              


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # game is won by one of the players
    if winner(board) != None:
        return True

    # moves still possible
    for row in board:
        if EMPTY in row:
            return False

    # no possible moves
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0
    
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -math.inf
            for action in actions(board):
                minival = min_value(result(board, action))[0]
                if minival > v:
                    v = minival
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = math.inf
            for action in actions(board):
                maxival = max_value(result(board, action))[0]
                if maxival < v:
                    v = maxival
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]