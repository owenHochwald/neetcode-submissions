class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        n, m = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] 

        q = deque()
        fruit = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fruit += 1
                elif grid[i][j] == 2:
                    q.append([i,j,0]) # x, y, mins
        
        while q:
            i, j, mins = q.popleft()
            time = max(mins, time)

            for dx, dy in dirs:
                x, y = i + dx, j + dy

                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                    grid[x][y] = 2
                    fruit -= 1
                    q.append([x,y,mins+1])







        return time if fruit == 0 else -1