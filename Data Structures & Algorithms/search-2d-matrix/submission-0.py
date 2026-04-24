class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        # First: find the correct row
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols - 1]:
                # Search inside this row
                l, r = 0, cols - 1
                while l <= r:
                    mid_col = (l + r) // 2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        l = mid_col + 1
                    else:
                        r = mid_col - 1
                return False
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        return False
