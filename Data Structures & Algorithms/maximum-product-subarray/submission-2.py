class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr = 1
        for num in nums:
            curr *= num
            max_prod = max(max_prod, curr)
            if num == 0:
                curr = 1
        curr = 1
        for num in reversed(nums):
            curr *= num
            max_prod = max(max_prod, curr)
            if num == 0:
                curr = 1
        return max_prod