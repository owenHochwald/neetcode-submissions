class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        def dfs(r, c):
            if (not (0<= r < n and 0<= c < m and board[r][c] == "O")):
                return
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # changing first and last columns
        for r in range(n):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][m-1] == "O":
                dfs(r, m-1)

        # changing first and last rows
        for c in range(m):
            if board[0][c] == "O":
                dfs(0, c)
            if board[n-1][c] == "O":
                dfs(n-1, c)

        # changing back
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"





        