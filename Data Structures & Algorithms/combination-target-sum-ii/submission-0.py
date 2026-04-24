class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        nums = candidates
        nums.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                out.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path, remaining - nums[i])
                path.pop()
        
        backtrack(0, [], target)
        return out

        