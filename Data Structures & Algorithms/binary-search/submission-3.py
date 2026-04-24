class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        idx = len(nums) // 2
        mid = nums[idx]

        if mid == target:
            return idx
        elif mid > target:
            return self.search(nums[:idx], target)
        else:
            res = self.search(nums[idx+1:], target)
            if res == -1:
                return -1
            return idx + res + 1