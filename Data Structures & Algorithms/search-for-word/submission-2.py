class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False

        def backtrack(i, j, pos, seen):
            # valid state
            if pos == len(word):
                self.res = True
                return
            # invalid state 1 - be able to tell if we're out of bounds
            if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]):
                return
            # invalid state 2 - we've already seen this position
            if (i, j) in seen:
                return 
            # invalid state 3 - current letter not in the word
            if board[i][j] != word[pos]:
                return
            # explore state - check all neighors, add to set, increase pos by 1
            else:
                seen.add((i, j))
                pos += 1
                backtrack(i+1, j, pos, seen)
                backtrack(i-1, j, pos, seen)
                backtrack(i, j-1, pos, seen)
                backtrack(i, j+1, pos, seen)
                seen.remove((i, j))
                


        for r in range(len(board)):
            for c in range(len(board[r])):
                backtrack(r, c, 0, set())
                if self.res:
                    self.res
        return self.res