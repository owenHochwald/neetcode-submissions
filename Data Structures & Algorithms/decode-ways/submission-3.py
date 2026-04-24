from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def helper(n):
            if not n:
                return 1
            if n[0] == "0":
                return 0
            # if len(n) > 1 and n[0] != "0":
            res = helper(n[1:])

            if len(n) > 1 and 10 <= int(n[:2]) <= 26:
                res += helper(n[2:])

            return res
        return helper(s)

            


            
            


        
        