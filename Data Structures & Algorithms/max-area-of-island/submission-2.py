class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.best = 0
        n, m = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1,0], [-1,0]]


        seen = set()
        def dfs(i, j):
            seen.add((i, j))

            count = 0 
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] and (x, y) not in seen:
                    count += 1 + dfs(x, y)
            return count

        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i, j) not in seen:
                    self.best = max(self.best, dfs(i, j) + 1)








        return self.best
        