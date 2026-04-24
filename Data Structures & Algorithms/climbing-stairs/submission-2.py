class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0, 1:1, 2:2}

        def helper(i):
            if i not in memo:
                memo[i] = helper(i-1) + helper(i-2)
            return memo[i]



        return helper(n)
        