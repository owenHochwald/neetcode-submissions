class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.q = deque()
        time = -1
        self.fresh_oranges = 0

  

        def in_range(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
        def process_neighbors(i, j):
            if in_range(i +1, j) and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                self.fresh_oranges -= 1
                self.q.append((i +1, j))

            if in_range(i -1, j) and grid[i - 1][j] == 1:
                grid[i -1][j] = 2
                self.fresh_oranges -= 1
                self.q.append((i -1, j))

            if in_range(i, j + 1) and grid[i][j+1] == 1:
                grid[i][j + 1] = 2
                self.fresh_oranges -= 1
                self.q.append((i, j + 1))

            if in_range(i, j - 1) and grid[i][j-1] == 1:
                grid[i][j - 1] = 2
                self.fresh_oranges -= 1
                self.q.append((i, j - 1))



        # add rotten oranges to the queue and count number of fresh
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.fresh_oranges += 1
                elif grid[row][col] == 2:
                    self.q.append((row, col))
        
        if not self.fresh_oranges:
            return 0

        # BFS traversal
        while self.q:
            for _ in range(len(self.q)):
                i, j = self.q.popleft()

                if in_range(i, j):
                    # add neighbors
                    process_neighbors(i, j)
                    
            time += 1





        # checking if we reached the end
        if self.fresh_oranges:
            return -1
        return time

        