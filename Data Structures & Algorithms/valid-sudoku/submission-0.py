class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validLine(row):
            nums = [x for x in row if x != "."]
            return len(nums) == len(set(nums)) and all(x in "123456789" for x in nums) 

        # validate row       
        for row in board:
            if not validLine(row):
                return False
        # validate cols
        cols = (list(zip(*board)))
        for col in cols:
            if not validLine(col):
                return False

        # val boxes
        n = len(board)
        for row in range(0, n, 3):
            for col in range(0, n, 3):
                box = [board[r][c] for r in range(row, row + 3) for c in range(col, col+3)]
                if not validLine(box):
                    return False

        
        return True


        
        