class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        first_row = any(matrix[0][j] == 0 for j in range(m))
        first_col = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                curr = matrix[i][j]
                if curr == 0:
                    # set the corresponding things in the matrix, to handling in second iter
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for c in range(1, m):
                    matrix[i][c] = 0
                    
        for j in range(1, m):
            if matrix[0][j] == 0:
                for r in range(1, n):
                    matrix[r][j] = 0

        if first_col:
            for i in range(n):
                matrix[i][0] = 0

        if first_row:
            for j in range(m):
                matrix[0][j] = 0 
        