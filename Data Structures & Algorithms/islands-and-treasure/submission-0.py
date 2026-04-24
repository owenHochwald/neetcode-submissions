class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        def inBounds(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c <len(grid[0]) and grid[r][c] != -1


        def addNeighbors(r, c, steps):
            if inBounds(r+1, c):
                q.append((r+1, c, steps+1))
            if inBounds(r-1, c):
                q.append((r-1, c, steps+1))
            if inBounds(r, c+1):
                q.append((r, c+1, steps+1))
            if inBounds(r, c-1):
                q.append((r, c-1, steps+1))


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            r, c, steps = q.popleft()

            if (r, c) not in visited:
                visited.add((r, c))

                if grid[r][c] == 2147483647:
                    grid[r][c] = steps
                
                addNeighbors(r, c, steps)






    

            

        
        