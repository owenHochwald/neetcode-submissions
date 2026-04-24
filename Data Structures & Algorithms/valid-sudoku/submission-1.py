class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                if (curr in rows[i] or
                    curr in cols[j] or
                    curr in squares[(i // 3, j // 3)]):
                    return False
                
                rows[i].add(curr)
                cols[j].add(curr)
                squares[(i // 3, j // 3)].add(curr)

        return True
        