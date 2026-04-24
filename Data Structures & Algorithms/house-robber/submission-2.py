class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {0: nums[0]}
        if len(nums) > 1:
            memo[1] = max(nums[1], memo[0])
        def dp(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = max(nums[n] + dp(n-2), dp(n-1))
                return memo[n]
        return dp(len(nums) - 1)