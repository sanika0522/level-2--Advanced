def is_safe(board, row, col, n):
         for i in range(col):
             if board[row][i] == 1:
                 return False
         for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
             if board[i][j] == 1:
                 return False
         for i, j in zip(range(row, n), range(col, -1, -1)):
             if board[i][j] == 1:
                 return False
         return True

def solve_n_queens_util(board, col, n):
         if col >= n:
             return True
         for i in range(n):
             if is_safe(board, i, col, n):
                 board[i][col] = 1
                 if solve_n_queens_util(board, col + 1, n):
                     return True
                 board[i][col] = 0
         return False

def solve_n_queens(n):
         board = [[0] * n for _ in range(n)]
         if not solve_n_queens_util(board, 0, n):
             print("Solution does not exist")
             return
         for row in board:
             print(" ".join(str(x) for x in row))

solve_n_queens(4)  # Example for 4-Queens
     