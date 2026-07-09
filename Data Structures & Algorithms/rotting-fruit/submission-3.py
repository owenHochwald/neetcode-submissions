class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the first rotten fruit
        # do you dfs through it?
        # but the number until remaining fruits is going to be the max
        # so basically we can do our dfs, but the deepest path is the answer!
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        n, m = len(grid), len(grid[0])
        q = deque() 
        fresh = 0


        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                if curr == 1:
                    fresh += 1
                if curr == 2:
                    q.append([i, j, 0])

        time = 0 
        while q:
            i, j, minutes = q.popleft()
            time = max(time, minutes)

            for dx, dy in dirs:
                ni, nj = dx + i, dy + j

                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    q.append([ni, nj, minutes + 1])

            



        
        return time if fresh == 0 else -1
