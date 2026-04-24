class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        largest = 0

        def dfs(i, j):
            if (i,j) in visited or not (i >= 0 and j >= 0 and i < len(grid) and j <len(grid[0])) or not grid[i][j]:
                return 0
            else:
                visited.add((i, j))

                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    largest = max(largest, dfs(i, j))

        return largest
        