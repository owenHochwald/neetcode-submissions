class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m = len(grid), len(grid[0])

        chests = deque()


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    chests.append([i, j, 0])
        
        # do a calm DFS for each chest
        dist = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while chests:
            r, c, d = chests.popleft()

            for dx, dy in dist:
                x, y = dx + r, dy + c
                if 0 <= x < n and 0 <= y < m and grid[x][y] == INF:
                    grid[x][y] = d + 1
                    chests.append([x, y, d+1])




        
        