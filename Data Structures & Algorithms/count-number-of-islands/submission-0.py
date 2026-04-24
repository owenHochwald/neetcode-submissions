class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        def inBounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c <len(grid[0]) and grid[r][c] != "0"

        def dfs(r, c):
            if (r, c) not in visited and inBounds(r, c):
                visited.add((r, c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count
        