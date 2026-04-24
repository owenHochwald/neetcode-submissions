class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0,0
        for first in range(0,len(nums)-1):
            for second in range(first+1, len(nums)):
                if nums[first] + nums[second] == target:
                    i = first
                    j = second
        return [i,j]
        