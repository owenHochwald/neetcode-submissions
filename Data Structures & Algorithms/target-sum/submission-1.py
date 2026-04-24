class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(curr, i):
            if i == len(nums):
                return 1 if curr == target else 0
            if (curr, i) not in memo:
                add = dfs(curr + nums[i], i + 1)
                sub = dfs(curr - nums[i], i + 1)
                memo[(curr, i)] = add + sub
            return memo[(curr, i)]
            
        count = dfs(0, 0)
        return count
        