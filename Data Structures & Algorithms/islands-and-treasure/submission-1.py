class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n = len(grid)
        m = len(grid[0])

        q = deque()
        seen = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j, 0])

        while q:
            r, c, count = q.popleft()

            if grid[r][c] == INF:
                grid[r][c] = count
            if grid[r][c] == -1:
                continue
            seen.add((r, c))

            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for x, y in directions:
                i, j = r + x, c + y
                if 0 <= i < n and 0 <= j < m and (i, j) not in seen:
                    q.append((i, j, count + 1))




