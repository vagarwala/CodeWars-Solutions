from math import sqrt
from math import floor
class Sudoku(object):
    def __init__(self, board):
        self.board = board
    def is_valid(self):
        board = self.board
        N = len(board)
        for row in board:
            if len(row) != N:
                return False
            for num in row:
                if type(num) != type(3):
                    return False
            if sorted(row) != list(range(1, N+1)):
                return False
        if not floor(sqrt(N)) == sqrt(N):
            return False
        n = int(sqrt(N))
        for i in range(N):
            if sorted([board[j][i] for j in range(N)]) != list(range(1, N+1)):
                return False
        for i in range(n):
            for j in range(n):
                box = []
                for x in range(n):
                    box += board[i*n + x][j*n:(j+1)*n]
                if sorted(box) != list(range(1, N+1)):
                    return False
        return True