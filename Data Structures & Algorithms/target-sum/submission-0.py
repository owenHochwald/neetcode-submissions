class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(curr, i):
            nonlocal count
            if i == len(nums) and curr == target:
                return 1
            if i >= len(nums):
                return 0
            else:
                add = dfs(curr + nums[i], i + 1)
                sub = dfs(curr - nums[i], i + 1)
                return add + sub
        count = dfs(0, 0)
        return count
        