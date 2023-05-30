class NQueens:
    def is_safe(self, board, row, col): #4
        # Vertically up
        for i in range(row - 1, -1, -1):
            if board[i][col] == 'Q':
                return False
        
        # Left diagonal up
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Right diagonal up
        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def n_queens(self, board, row): #2
        if row == len(board):
            self.print_board(board)
            self.count += 1
            return
        
        for j in range(len(board)):
            if self.is_safe(board, row, j):
                # Place a queen in each row
                board[row][j] = 'Q'
                self.n_queens(board, row + 1)
                board[row][j] = 'x'

    def print_board(self, board):   #3
        print("---Chess Board---")
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end=" ")
            print()
    
    def solve_n_queens(self, n):  #1
        board = [['x'] * n for _ in range(n)]
        self.count = 0
        
        self.n_queens(board, 0)
        print("Total number of solutions: ", self.count)
        

if __name__ == "__main__":
    n = 6
    queens = NQueens()
    queens.solve_n_queens(n)
    
    # O(N!) O(N)

