class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(start, total):
            if start == len(nums):
                return total

            # take or skip
            return dfs(start +1, total ^ nums[start]) + dfs(start+1, total)
        return dfs(0, 0)