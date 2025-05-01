class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def construct(board):
            return ["".join(row) for row in board]

        def is_safe(row, col):
            # ⬅️ Left Row
            for c in range(col):
                if board[row][c] == 'Q':
                    return False
            # ↖️ Upper-Left Diagonal
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            # ↙️ Lower-Left Diagonal
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1
            return True

        def backtrack(col):
            if col == n:
                solutions.append(construct(board))
                return
            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'  # \U0001f451
                    backtrack(col + 1)
                    board[row][col] = '.'  # \U0001f501 backtrack

        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        backtrack(0)
        return solutions