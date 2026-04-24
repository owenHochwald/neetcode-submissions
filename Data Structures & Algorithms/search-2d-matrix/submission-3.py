class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary search to find the row (checking start <= target <= end)
        l, r = 0, len(matrix)-1

        while l <= r:
            m = (l+r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return self.searchRow(matrix[m], target)
            elif matrix[m][-1] <= target:
                l = m + 1
            else:
                r = m - 1
        return False

        
    def searchRow(self, row, target):
        l, r = 0, len(row)-1
        while l < r:
            m = (l+r) //2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m
            else:
                l = m +1
        return row[l] == target
        