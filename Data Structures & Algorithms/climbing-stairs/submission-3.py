class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(i):
            if i <= 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i not in memo:
                memo[i] = helper(i-1) + helper(i-2)
            return memo[i]



        return helper(n)
        