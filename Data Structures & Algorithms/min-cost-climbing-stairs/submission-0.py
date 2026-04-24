class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:0, 1:0}

        def dp(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
                return memo[n]
        dp(len(cost))
        return memo[len(cost)]