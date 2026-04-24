class NumMatrix:
    # compute prefix sum array for each row in the matrix
    # literally just query the prefix sum for a row iterable and sum to a total

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.buildPrefixMatrix()


    def buildPrefixMatrix(self):
        m, n = len(self.matrix), len(self.matrix[0])

        matrix = [[self.matrix[i][j] for j in range(n)] for i in range(m)]
        
        # precompute the first row
        for i in range(1, n):
            matrix[0][i] += matrix[0][i-1]

        # precompute the second row
        for i in range(1, m):
            matrix[i][0] += matrix[i-1][0]
        
        # do curr[i][j] = curr[i-1][j] + curr[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix
                




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        total = matrix[row2][col2]

        top = matrix[row1-1][col2] if row1 > 0 else 0
        left = matrix[row2][col1-1] if col1 > 0 else 0
        overlap = matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0


        return total - top - left + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)





