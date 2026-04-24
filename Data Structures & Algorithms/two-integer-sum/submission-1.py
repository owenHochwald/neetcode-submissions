class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in lookup:
                return [lookup[need], i]
            lookup[num] = i
        return -1
        