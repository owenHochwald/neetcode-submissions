class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]

        if og_color == color:
            return image

        n, m = len(image), len(image[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            image[i][j] = color

            for dx, dy in dirs:
                x, y = i + dx, j + dy

                if 0 <= x < n and 0 <= y < m and image[x][y] == og_color:
                    dfs(x, y)

        dfs(sr, sc)
        return image