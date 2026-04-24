class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, start, curr):
            if curr == target:
                res.append(path[:])
                return
            elif curr > target:
                return
            else:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(path, i, curr + nums[i])
                    path.pop()

        backtrack([], 0, 0)
        return res
        