class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()
        q_p = deque()
        q_a = deque()

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                    q_p.append((i, j))
                if i == n -1 or j == m - 1:
                    atlantic.add((i, j))
                    q_a.append((i, j))
        
        def bfs(q, seen):
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        x, y = i + a, j + b

                        if (x, y) not in seen and 0 <= x < n and 0 <= y < m and heights[x][y] >= heights[i][j]:
                            seen.add((x, y))
                            q.append((x, y))
            return seen

        atlantic = bfs(q_a, atlantic)
        pacific = bfs(q_p, pacific)

        res = []

        for x, y in pacific:
            if (x, y) in atlantic:
                res.append([x, y])
        return res

        