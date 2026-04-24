class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def dfs(r, c):
            if (r,c) in seen:
                return 0
            seen.add((r,c))

            curr = 0

            for dx, dy in directions:
                x, y = dx+r, dy+c
                if 0 > x or x >= len(grid) or 0 > y or y >= len(grid[0]) or grid[x][y] == 0:
                    curr += 1
                elif (x, y) not in seen:
                    curr += dfs(x, y)


            return curr

            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

        