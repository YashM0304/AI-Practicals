class NQueens:
    def __init__(self, n):
        self.n = n
        self.result = []

    def solve(self):
        board = [-1] * self.n
        self.place_queen(board, 0)
        return self.result

    def place_queen(self, board, row):
        if row == self.n:
            self.result.append(board[:])
        else:
            for col in range(self.n):
                if self.is_safe(board, row, col):
                    board[row] = col
                    self.place_queen(board, row + 1)
                    board[row] = -1

    def is_safe(self, board, row, col):
        for i in range(row):
            if (
                board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row
            ):
                return False
        return True
n = 4
n_queens = NQueens(n)
solutions = n_queens.solve()

for solution in solutions:
    print(solution)