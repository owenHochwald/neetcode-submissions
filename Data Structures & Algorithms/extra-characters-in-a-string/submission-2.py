class Node:
    def __init__(self):
        self.terminal = False
        self.children = []

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)

        memo = {} 

        def solve(i ):
            if i >= len(s):
                return 0

            if i in memo:
                return memo[i] 
            # skip -> add one because it counts as "skipping"
            res = 1 + solve(i+1)

            for j in range(len(s)):
                if s[i:j+1] in words:
                    res = min(res, solve(j+1))

            memo[i] = res
            
            return res

        return solve(0)






