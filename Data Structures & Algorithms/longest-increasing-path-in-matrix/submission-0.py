class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        n, m = len(matrix), len(matrix[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < m):
                return
            if (r,c) not in memo:
                # get the current cell
                memo[(r,c)] = 1
                curr = matrix[r][c]

                # check all the moveable directiosn to find increasing
                for dx, dy in directions:
                    if (0 <= r+dx < n and 0 <= c+dy < m):
                        move = matrix[r+dx][c+dy]

                        if move > curr:
                            memo[(r,c)] = max(memo[(r,c)], dfs(r+dx, c+dy)+1)

            return memo[(r,c)]




        res = 0

        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i,j))

        return res