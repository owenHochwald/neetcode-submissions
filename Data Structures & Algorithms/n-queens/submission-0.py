class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diag1, diag2 = set(), set(), set()

        out = []

        def backtrack(board, queens, row):
            if queens == n:
                out.append([''.join(b) for b in board])
                return
            else:
                for col in range(n):
                    if col in cols or (row+col) in diag1 or (row-col) in diag2:
                        continue
                    
                    cols.add(col)
                    diag1.add((row+col))
                    diag2.add((row-col))
                    board[row][col] = 'Q'
                    backtrack(board, queens+1, row+1)
                    board[row][col] = '.'
                    cols.remove(col)
                    diag1.remove((row+col))
                    diag2.remove((row-col))



        board = [["."] * n for _ in range(n)]
        backtrack(board, 0, 0)
        return out