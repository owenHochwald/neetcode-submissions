class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = set()
        n = len(nums)
        used = [False] * n

        def dfs(path):
            if len(path) == len(nums):
                out.add(tuple(path))

            for i in range(n):
                if used[i]:
                    continue

                used[i] = True 
                dfs(path + [nums[i]])

                used[i] = False 

        dfs([])
        return list(out)
