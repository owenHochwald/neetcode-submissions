class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n, m = len(matrix), len(matrix[0])
        l, r = 0, m
        t, b = 0, n

        while l < r and t < b:
            # top row -> left -> right
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # right column -> top -> bottom
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1

            # insurance
            if not (l < r and t < b):
                break
            
            # bottom row -> right -> left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b-1][i])
            b -= 1

            # left col -> bottom - > top
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1



        return res

        