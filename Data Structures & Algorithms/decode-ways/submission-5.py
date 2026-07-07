from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # if the last two digits range from 10-26 then there are two ways
        # if there is just one digit from 1-9 its just 1 ways
        # if its a zero, there is invalid and belongs with the other one

        n = len(s)
        @cache
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if s[i] == "0":
                return 0
            
            res = dfs(i+1) 

            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            return res


        
        return dfs(0)