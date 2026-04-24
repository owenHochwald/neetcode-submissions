class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(combo, oc, cc):
            if oc == cc == n and len(combo) == n*2:
                res.append(combo)
                return
            else:
                if cc > oc or oc > n or cc > n:
                    return
                backtrack(combo + "(", oc+1, cc)
                backtrack(combo + ")", oc, cc+1)
        
        backtrack("", 0, 0)
        return res
                


        