class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        n, m = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            if (r, c) in seen or not (0 <= r < n and 0 <= c < m and grid[r][c]):
                return 0

            seen.add((r,c))
            

            out = 1
            directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
            for dx, dy in directions:
                out += dfs(r + dx, c + dy)

            return out


        # if we haven't seen a 1 pos before, explore!
        for i in range(n):
            for j in range(m):        
                if grid[i][j] == 1 and (i, j) not in seen:
                    area = max(area, dfs(i, j))


        return area