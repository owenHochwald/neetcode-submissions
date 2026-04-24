from functools import cache 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @cache
        def dfs(i):
            if i == 0:
                return 1
            res = 0

            for num in nums:
                if i < num:
                    break
                res += dfs(i - num)

            return res

        return dfs(target)
