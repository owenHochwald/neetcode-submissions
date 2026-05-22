class Node:
    def __init__(self):
        self.terminal = False
        self.children = []

from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)

        memo = dict()

        @cache
        def solve(i ):
            if i >= len(s):
                return 0
            
            # skip -> add one because it counts as "skipping"
            res = 1 + solve(i+1)

            for j in range(len(s)):
                if s[i:j+1] in words:
                    res = min(res, solve(j+1))
            
            return res

        return solve(0)






