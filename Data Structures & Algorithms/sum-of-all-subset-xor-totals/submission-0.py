class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        paths = []
        

        def dfs(i, path):
            if len(path) <= len(nums):
                paths.append(path[:])
                for j in range(i, len(nums)):
                    dfs(j+1, path + [nums[j]])
            
        dfs(0, [])
        for path in paths:
            curr = 0
            for num in path:
                curr ^= num
            total += curr
        return total

