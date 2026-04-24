class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open_count 
        # closed_count <= open_count
        # valid when both == n
        # closed_count can never be more than the open count
        # n = 2
        #  "(", cc=0, oc=1), (")", cc=1, oc=0) -> INVALID
        # ("((", cc=0, oc=2), ("()", cc=1, oc=1)
        # ("(()", cc=1, oc=2), ("(()", cc=1, oc=3)-> INVALID,
            # ("())", cc=2, oc=1)-> INVALID,  ("()(", cc=1, oc=2)
        # out = ["(())", "()()"]
        out = []

        def backtrack(curr, cc, oc):
            if cc > oc or oc > n or cc > n:
                return
            if cc == n and oc == n:
                out.append(curr)
                return
            else:
                backtrack(curr + "(", cc, oc+1)
                backtrack(curr + ")", cc+1, oc)

        backtrack("", 0, 0)
        return out


        