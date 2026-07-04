class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = list()


        def dfs(path, remain, start):
            if remain == 0:
                
                out.append(path[:])
            if remain < 0:
                return 

            for i in range(start, len(nums)):

                dfs(path + [nums[i]], remain - nums[i], i)

        dfs([], target, 0)
        return out