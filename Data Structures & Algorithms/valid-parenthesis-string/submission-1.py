from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, oo):
            if oo < 0:
                return False
            if i == len(s):
                if not oo:
                    return True
                return False

            c = s[i] 
            if c == "(":
                return dfs(i+1, oo+1) 
            elif c == ")":
                return dfs(i+1, oo-1) 
            
            return (
                dfs(i+1, oo) or
                dfs(i+1, oo+1) or
                dfs(i+1, oo-1)
            )

        return dfs(0, 0)
        