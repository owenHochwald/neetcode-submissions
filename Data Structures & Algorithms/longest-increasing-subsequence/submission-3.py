from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i, prev):
            if i == n:
                return 0
            
            # skip
            best = dfs(i+1, prev)

            # take (if we actually can)
            if nums[i] > prev:
                best = max(best, 1 + dfs(i+1, nums[i]))
            return best
            

        return dfs(0, float('-inf'))
